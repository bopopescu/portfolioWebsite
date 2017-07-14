$(document).ready(function(){
    var active_indicator = $('.carousel-indicators').children('li').first();
    active_indicator.addClass("active");
    var active_item = $('.carousel-inner').children('.carousel-item').first();
    active_item.addClass("active");

    //change size of displayed images when browser changes size
    $(window).resize(function() {
        $('.carousel-item img').width($('#mainCarousel').width());
    });

    //Everything to run on start
    $('.carousel-item img').width($('#mainCarousel').width());
});
