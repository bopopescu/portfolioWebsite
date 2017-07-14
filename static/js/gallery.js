//gallery.js

$(document).ready(function() {
    var slideer = $("#light-slider").lightSlider({
        vertical:true,
        item:3,
        loop:false,
        enableTouch:true,
        enableDrag:true,
        freeMove:true,
        controls:true,
        adaptiveHeight:false,
        prevHtml:"<img src=\"/static/images/up-arrow.png\"/>",
        nextHtml:"<img src=\"/static/images/down-arrow.png\"/>",
        slideMargin:10
    });

    $(window).resize(function() {
        //$('#light-slider img').width($('.img-slide-box li').width());
        var item = 2;
        var verticalHeight = item * $('.img-slide-box') + item * 10;
        slider = $("#light-slider").lightSlider({
            vertical:true,
            item:item,
            loop:false,
            enableTouch:true,
            enableDrag:true,
            freeMove:true,
            controls:true,
            adaptiveHeight:false,
            prevHtml:"<img src=\"/static/images/up-arrow.png\"/>",
            nextHtml:"<img src=\"/static/images/down-arrow.png\"/>",
            slideMargin:10,
            verticalHeight:verticalHeight
        });
        slider.refresh();
        $('#light-slider img').height($('.img-slide-box').height());
        $('.lSPager').hide();
    });

    //Everything to run on start
    $('.lSPager').hide();
    $('#light-slider img').height($('.img-slide-box').width());
});
