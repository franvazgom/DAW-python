$(function(){ 
    $("#btn1").click(function(){
        $("#tabla1 tr:odd").css('background', '#c1c1c1');
        //$("tr:odd").css('background', '#c1c1c1');
    });
    $("#tabla1 tr").mouseover(function(){
        $(this).css('background', 'yellow');
    });
    $("#tabla1 tr").mouseleave(function(){
        $(this).css('background', 'white');        
    });
    $("#tabla1 tr").dblclick(function(){
        console.log('ddddddd');
        $("#caja1").val('44');
    });
});