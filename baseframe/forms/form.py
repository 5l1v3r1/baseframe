# -*- coding: utf-8 -*-

import six

from threading import Lock
import uuid

from flask import current_app
from flask_wtf import FlaskForm as BaseForm
from speaklater import is_lazy_string
from wtforms.compat import iteritems
import wtforms

from .. import asset_cache
from .. import b__ as __
from ..signals import form_validation_error, form_validation_success
from . import fields as bfields
from . import filters as bfilters
from . import parsleyjs as bparsleyjs
from . import validators as bvalidators

__all__ = [
    'field_registry',
    'widget_registry',
    'validator_registry',
    'Form',
    'FormGenerator',
    'RecaptchaForm',
]

# Use a hardcoded list to control what is available to user-facing apps
field_registry = {
    'SelectField': bparsleyjs.SelectField,
    'SelectMultipleField': bfields.SelectMultipleField,
    'RadioField': bparsleyjs.RadioField,
    'StringField': bparsleyjs.StringField,
    'IntegerField': bparsleyjs.IntegerField,
    'DecimalField': bparsleyjs.DecimalField,
    'FloatField': bparsleyjs.FloatField,
    'BooleanField': bparsleyjs.BooleanField,
    'TelField': bparsleyjs.TelField,
    'URLField': bparsleyjs.URLField,
    'EmailField': bparsleyjs.EmailField,
    'DateTimeField': bfields.DateTimeField,
    'DateField': bparsleyjs.DateField,
    'TextAreaField': bparsleyjs.TextAreaField,
    'PasswordField': bparsleyjs.PasswordField,
    # Baseframe fields
    'RichTextField': bfields.TinyMce4Field,
    'TextListField': bfields.TextListField,
    'UserSelectField': bfields.UserSelectField,
    'UserSelectMultiField': bfields.UserSelectMultiField,
    'GeonameSelectField': bfields.GeonameSelectField,
    'GeonameSelectMultiField': bfields.GeonameSelectMultiField,
    'AnnotatedTextField': bfields.AnnotatedTextField,
    'MarkdownField': bfields.MarkdownField,
    'ImageField': bfields.ImgeeField,
}

widget_registry = {}

validator_registry = {
    'Length': (wtforms.validators.Length, 'min', 'max', 'message'),
    'NumberRange': (wtforms.validators.NumberRange, 'min', 'max', 'message'),
    'Optional': (wtforms.validators.Optional, 'strip_whitespace'),
    'Required': (wtforms.validators.DataRequired, 'message'),
    'AnyOf': (wtforms.validators.AnyOf, 'values', 'message'),
    'NoneOf': (wtforms.validators.NoneOf, 'values', 'message'),
    'ValidEmail': bvalidators.ValidEmail,
    'ValidUrl': bvalidators.ValidUrl,
    'AllUrlsValid': bvalidators.AllUrlsValid,
}

filter_registry = {
    'lower': (bfilters.lower,),
    'upper': (bfilters.upper,),
    'strip': (bfilters.strip, 'chars'),
    'lstrip': (bfilters.lstrip, 'chars'),
    'rstrip': (bfilters.rstrip, 'chars'),
    'none_if_empty': (bfilters.none_if_empty),
}


_nonce_lock = Lock()


def _nonce_cache_key(nonce):
    return 'form_nonce/' + nonce


def _nonce_validator(form, field):
    # Check for already-used form nonce
    if field.data:
        with _nonce_lock:
            # nonce_lock prevents parallel requests from attempting to use the same
            # nonce in a multi-threaded deployment. As a thread lock, it is ineffective
            # in a multi-process deployment, as is typical when using uwsgi or gunicorn.
            nonce_cache_key = _nonce_cache_key(field.data)
            nonce_cache_hit = asset_cache.get(nonce_cache_key)
            if nonce_cache_hit is not None:
                raise bvalidators.StopValidation(form.form_nonce_error)
            # Mark this nonce as used for 10 seconds
            asset_cache.set(_nonce_cache_key(field.data), True, 10)
        # Set a new nonce. This is a conscious deviation from the convention for
        # validators, which are expected to validate but not modify the data, leaving
        # that to filters. However, filters run before validators, and the form nonce
        # is nonsense data that will be imminently discarded, so this is okay here.
        field.data = field.default()


class Form(BaseForm):
    """
    Form with additional methods.
    """

    __expects__ = ()
    __returns__ = ()

    form_nonce = bfields.NonceField(
        "Nonce", validators=[_nonce_validator], default=lambda: uuid.uuid4().hex
    )
    form_nonce_error = __("This form has already been submitted")

    def __init_subclass__(cls, **kwargs):
        """
        Validate :attr:`__expects__` and :attr:`__returns__` in sub-classes
        """
        super().__init_subclass__(**kwargs)
        if {'edit_obj', 'edit_model', 'edit_parent', 'edit_id'} & set(cls.__expects__):
            raise TypeError(
                "This form has __expects__ parameters that are reserved by the base form"
            )

        if set(cls.__dict__.keys()) & set(cls.__expects__):
            raise TypeError(
                "This form has __expects__ parameters that clash with field names"
            )

    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        for attr in self.__expects__:
            if attr not in kwargs:
                raise TypeError("Expected parameter %s was not supplied" % attr)
            setattr(self, attr, kwargs.pop(attr))

        # Make editing objects easier
        self.edit_obj = kwargs.get('obj')
        self.edit_model = kwargs.get('model')
        self.edit_parent = kwargs.get('parent')
        if self.edit_obj:
            if hasattr(self.edit_obj, 'id'):
                self.edit_id = self.edit_obj.id
            else:
                self.edit_id = None
            if not self.edit_model:
                self.edit_model = self.edit_obj.__class__
            if not self.edit_parent and hasattr(self.edit_obj, 'parent'):
                self.edit_parent = self.edit_obj.parent
        else:
            self.edit_id = None
        self.set_queries()

    def validate(self, send_signals=True):
        success = super(Form, self).validate()
        for attr in self.__returns__:
            if not hasattr(self, attr):
                setattr(self, attr, None)
        if send_signals:
            self.send_signals()
        return success

    def send_signals(self):
        if self.errors:
            form_validation_error.send(self)
        else:
            form_validation_success.send(self)

    def errors_with_data(self):
        # Convert lazy_gettext error strings into unicode so they don't cause problems downstream
        # (like when pickling)
        return {
            name: {
                'data': f.data,
                'errors': [
                    six.text_type(e) if is_lazy_string(e) else e for e in f.errors
                ],
            }
            for name, f in iteritems(self._fields)
            if f.errors
        }

    def set_queries(self):
        """
        Override this method in the sub-class to set queries that might
        be required for form fields such as QuerySelectField or QuerySelectMultipleField
        """


class FormGenerator(object):
    """
    Creates forms from a JSON-compatible dictionary structure
    based on the allowed set of fields, widgets, validators and filters.
    """

    def __init__(
        self,
        fields=None,
        widgets=None,
        validators=None,
        filters=None,
        default_field='StringField',
    ):
        # If using global defaults, make a copy in this class so that
        # they can be customised post-init without clobbering the globals
        self.fields = fields or dict(field_registry)
        self.widgets = widgets or dict(widget_registry)
        self.validators = validators or dict(validator_registry)
        self.filters = filters or dict(filter_registry)

        self.default_field = default_field

    def generate(self, formstruct):
        """
        Generate a dynamic form from the given data structure.
        """

        class DynamicForm(Form):
            pass

        for fielddata in formstruct:
            fielddata = dict(fielddata)  # Make a copy
            name = fielddata.pop('name', None)
            type_ = fielddata.pop('type', None)
            if not name:
                continue  # Skip unnamed fields
            if (not type_) or type_ not in field_registry:
                type_ = self.default_field  # Default to string input

            # TODO: Process widget requests

            # Make a list of validators
            validators = []
            validators_data = fielddata.pop('validators', [])
            for item in validators_data:
                if isinstance(item, six.string_types) and item in validator_registry:
                    validators.append(validator_registry[item][0]())
                else:
                    itemname = item.pop('type', None)
                    itemparams = {}
                    if itemname:
                        for paramname in item:
                            if paramname in validator_registry[itemname][1:]:
                                itemparams[paramname] = item[paramname]
                        validators.append(validator_registry[itemname][0](**itemparams))

            # Make a list of filters
            filters = []
            filters_data = fielddata.pop('filters', [])
            for item in filters_data:
                if isinstance(item, six.string_types) and item in filter_registry:
                    filters.append(filter_registry[item][0]())
                else:
                    itemname = item.pop('type', None)
                    itemparams = {}
                    if itemname:
                        for paramname in item:
                            if paramname in filter_registry[itemname][1:]:
                                itemparams[paramname] = item[paramname]
                        filters.append(filter_registry[itemname][0](**itemparams))

            # TODO: Also validate the parameters in fielddata, like with validators above
            setattr(
                DynamicForm,
                name,
                field_registry[type_](
                    validators=validators, filters=filters, **fielddata
                ),
            )
        return DynamicForm


class RecaptchaForm(Form):
    recaptcha = bfields.RecaptchaField()

    def __init__(self, *args, **kwargs):
        super(RecaptchaForm, self).__init__(*args, **kwargs)
        if not (
            current_app.config.get('RECAPTCHA_PUBLIC_KEY')
            and current_app.config.get('RECAPTCHA_PRIVATE_KEY')
        ):
            del self.recaptcha
