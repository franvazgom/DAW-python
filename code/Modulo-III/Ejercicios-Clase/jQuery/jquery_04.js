11111111111/* 
Comentario multilinea
*/
$(function(){
    $('#btn1').click(function(){
        if ($(this).text() == "Cambia formato de table") {
            $("#tablaNombres tr:odd").css('background', '#c1c1c1');
            $(this).text("Elimina formato");
        } else {
            $("#tablaNombres tr:odd").css('background', 'white');
            $(this).text("Cambia formato de table");
        }
    });
    $('p').mouseenter(function(){
        $(this).hide(1000);
    });
    $('p').mouseleave(function(){
        $(this).show(1000);
    });
    $('#table2 tr').mouseover(function(){
        $(this).css('background', 'yellow');
    });
    $('#table2 tr').mouseleave(function(){
        $(this).css('background', 'white');
    });
    $("tr").dblclick(function(){
        // $('#box1').val($(this).text());
        $('#box1').val($(this).find("td").eq(-2).text());
    });
    cambiaTexto();
});

function cambiaTexto() {
    $('#btnP').text("ABC"); 
}
