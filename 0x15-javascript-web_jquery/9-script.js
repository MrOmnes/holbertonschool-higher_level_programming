$.get('https://fourtonfish.com/hellosalut/?lang=fr?format=json', window.onload = function (data) {
    $('DIV#hello').text(data);
});
