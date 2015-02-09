# -*- coding: utf-8 -*-

from flask import current_app
from flask.signals import Namespace

baseframe_signals = Namespace()

form_validation_error = baseframe_signals.signal('form-validation-error')
form_validation_success = baseframe_signals.signal('form-validation-success')
exception_catchall = baseframe_signals.signal('exception-catchall')


@form_validation_error.connect
def log_error(form):
    current_app.logger.info("Form Validation Error: %r" % form.errors)


@form_validation_success.connect
def log_success(form):
    current_app.logger.info("Form Validation Success: %r" % form.errors)


@exception_catchall.connect
def log_catchall(e):
    current_app.logger.info("Exception: %r" % e)
