window.onload = function () {

    $('DIV#add_item').click(function (event) {
        $('UL.my_list').append('<li>Item</li>');
    });

    $('DIV#remove_item').click(function (event) {
        $('UL.my_list li:last-child').remove();
    });

    $('DIV#clear_list').click(function (event) {
        $('UL.my_list').empty();
    });

}
