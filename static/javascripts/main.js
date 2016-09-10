var STATUS_URL = 'http://hackerdeen.org/spaceapi';

$(document).ready(function () {
  $.getJSON(STATUS_URL)
    .done(function (json) {
      if (json.state.open) {
        $('#status').text('open');
      } else {
        $('#status').text('closed');
      }
      $('#status-message').text(json.state.message);
    })
    .fail(function () {
      $('#status').text('unknown');
      $('#status-message').text('unknown');
    });
});
