
$(function(){
    $('#btnHideShow').click(efectoHideShow);
    $('#btnFadeInOut').click(efectoFadeInOut);
    $('#btnSlideDownUp').click(efectoSlideDownUp);
});

function efectoHideShow() {
    if ($('#pHideShow').is(":visible")){
        $('#pHideShow').hide(1500);
        $('#btnHideShow').text('Show');
    }else {
        $('#pHideShow').show("fast");
        $('#btnHideShow').text('Hide');
    }
}

function efectoFadeInOut() {
    /* Para divFadeInOut mediante btnFadeInOut y utilizando fadeOut y fadeIn */    
}

function efectoSlideDownUp() {
    /* Para divSlideDownUp mediante btnSlideDownUp y utilizando slideUp y slideDown */    
}