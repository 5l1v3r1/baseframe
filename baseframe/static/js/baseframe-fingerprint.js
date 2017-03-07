if (typeof window.Baseframe === "undefined") {
  window.Baseframe = {
  };
};

window.Baseframe.browser_fingerprint = function() {
  var options = {excludeIEPlugins: true};
  new Fingerprint2(options).get(function(result, components) {
    $.ajax('/api/baseframe/1/fingerprint/submit', {
      method: 'POST',
      contentType: 'application/json; charset=utf-8',
      dataType: 'json',
      data: JSON.stringify({'fingerprint': result, 'components': components})
    })
  });
}

$(function() {
  window.Baseframe.browser_fingerprint();  
});
