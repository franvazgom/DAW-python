$(function() {
    $('tr').mouseenter(function(){
        $(this).css('background', 'yellow');
    });
    $('tr').mouseleave(function(){
        $(this).css('background', 'white');
    });
    $('#tabla1 tr').dblclick(function(){
        console.log($(this).text());
        //$('#caja1').val($(this).text());
        $('#caja1').val($(this).find('td').eq(0).text());
    });
});