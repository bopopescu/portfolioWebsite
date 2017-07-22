//gallery.js

$(document).ready(function() {

    var comment_slider = $("#comment-slider").lightSlider({
        item: 1,
        loop: false,
        enableTouch: false,
        enableDrag: false,
        freeMove: false,
        controls: false,
        adaptiveHeight: false
    });

    var slider = $("#slider-gallery").lightSlider({
        gallery: true,
        thumbItem: 5,
        item: 1,
        loop: false,
        enableTouch: true,
        enableDrag: true,
        freeMove: true,
        controls: true,
        adaptiveHeight: false,
        prevHtml: "<img src=\"/static/resource_imgs/left-chevron.png\"/>",
        nextHtml: "<img src=\"/static/resource_imgs/right-chevron.png\"/>",
        slideMargin: 10,
        onAfterSlide: function(el) {
            imageResize();
        },
        onBeforeSlide: function(el){
            comment_slider.goToSlide(slider.getCurrentSlideCount() -1);
        },
        onBeforeNextSlide: function(el) {
            comment_slider.goToNextSlide();
        },
        onBeforePrevSlide: function(el) {
            comment_slider.goToPrevSlide();
        }
    });



    $(window).resize(function() {
        //$('#light-slider img').width($('.img-slide-box li').width());

        imageResize();
    });

    //Everything to run on start
    //$('#light-slider img').width($('.img-slide-box').width());
    var imageResize = function() {
        $('.lslide').height($('#main-gallery').width() * .66);
        $('#slider-gallery img').each(function() {
            if ($(this).width() < $(this).height()) { //vertical
                $(this).height($('.lslide').height());
            } else { //horizontal
                $(this).width($('.lslide').width());
            }
        });
    };

    var thumbGalleryResize = function() {
        var lowestImg = Infinity;
        $('.lSGallery img').each(function() {
            if ($(this).height() < lowestImg) {
                lowestImg = $(this).height();
            }
        });
        $('.lSPager .lSGallery').height(lowestImg);
    }
    imageResize();
    thumbGalleryResize();



    $('#comments .lSPager').hide();
});
