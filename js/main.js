$(function () {
    $('.slider__park').slick({
        arrows: false,
        asNavFor: '.slider__inner',
        slidesToShow: 1,
        slidesToScroll: 1,
    });


    $('.slider__inner').slick({
        slidesToShow: 1,
        centerMode: true,
        slidesToScroll: 1,
        speed: 500,
        vertical: true,
        centerMode: true,
        arrows: false,
        dots: true,
        focusOnSelect: true,
        asNavFor: '.slider__park',
        // infinite: false,
        responsive: [
            {
                breakpoint: 1120,
                settings: {
                    vertical: false,
                }
            },
        ]


    });



    $('.slider-2').slick({
        slidesToShow: 2,
        centerMode: true,
        slidesToScroll: 1,
        infinite: true,
        arrows: false,
        dots: true,
        focusOnSelect: true,
    });

    $('.header-top__menu-btn').on('click', function () {
        $('.header-top__menu > ul').slideToggle();
    });
});