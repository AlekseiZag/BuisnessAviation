$(function () {
    $('.header-top__menu-btn').click(function () {
        $('.header-top__menu-btn div:nth-child(1)').toggleClass('first');
        $('.header-top__menu-btn div:nth-child(2)').toggleClass('middle');
        $('.header-top__menu-btn div:nth-child(3)').toggleClass('last');
    });


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

    $('.slider-card').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        vertical: false,
        speed: 500,
        arrows: false,
        dots: true,
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

    // $('select').styler();

    $('.header-top__menu-btn').on('click', function () {
        $('.header-top__menu > ul').slideToggle();
    });

    $('.icon-list').on('click', function () {
        $('.fleet__item').addClass('list');
        $('.icon-list').addClass('active');
        $('.icon-large').removeClass('active');
    });
    $('.icon-large').on('click', function () {
        $('.fleet__item').removeClass('list');
        $('.icon-large').addClass('active');
        $('.icon-list').removeClass('active');
    });


    $('.card__tabs .tab').on('click', function (event) {
        var id = $(this).attr('data-id');
        $('.card__tabs').find('.tab__item').removeClass('active-tab').hide();
        $('.card__tabs .tabs').find('.tab').removeClass('active');
        $(this).addClass('active');
        $('#' + id).addClass('active-tab').fadeIn();
        return false;
    });




});
document.addEventListener("DOMContentLoaded", function () {
    let phoneInputs = document.querySelectorAll('input[data-tel-input]')


    let getInputNumbersValue = function (input) {
        return input.value.replace(/\D/g, "")
    }

    let onPhoneInput = function (e) {
        let input = e.target,
            inputNumbersValue = getInputNumbersValue(input),
            formatedInputValue = "",
            selectionStart = input.selectionStart;

        if (!inputNumbersValue) {
            return input.value = "";
        }

        if (input.value.length != selectionStart) {
            console.log('Редактирование в середине строки', e);
            if (e.data && /\D/g.test(e.data)) {
                input.value = inputNumbersValue;
            }
            return;
        }

        if (["7", "8", "9"].indexOf(inputNumbersValue[0]) > -1) {
            // russian 
            if (inputNumbersValue[0] == "9") inputNumbersValue = "7" + inputNumbersValue;
            let firstsymbols = (inputNumbersValue[0] == "8") ? "8" : "+7";
            formatedInputValue = firstsymbols + " ";
            if (inputNumbersValue.length > 1) {
                formatedInputValue += "(" + inputNumbersValue.substring(1, 4);
            }
            if (inputNumbersValue.length >= 5) {
                formatedInputValue += ") " + inputNumbersValue.substring(4, 7);
            }
            if (inputNumbersValue.length >= 8) {
                formatedInputValue += "-" + inputNumbersValue.substring(7, 9);
            }
            if (inputNumbersValue.length >= 10) {
                formatedInputValue += "-" + inputNumbersValue.substring(9, 11);
            }
        } else {
            console.log('not ru')
            // not russian
            formatedInputValue = "+" + inputNumbersValue.substring(0, 15);
        }
        input.value = formatedInputValue;
    }



    let onPhoneKeydown = function (e) {
        let input = e.target;
        if (e.keyCode == 8 && getInputNumbersValue(input).length == 1) {
            input.value = "";
        }
    }
    let onPhonePaste = function (e) {
        let pasted = e.clipboardData || window.clipboardData,
            input = e.target,
            inputNumbersValue = getInputNumbersValue(input);

        if (pasted) {
            let pastedText = pasted.getData("Text");
            if (/\D/g.test(pastedText)) {
                input.value = inputNumbersValue;
            }
        }
    }
    for (i = 0; i < phoneInputs.length; i++) {
        let input = phoneInputs[i];
        input.addEventListener("input", onPhoneInput);
        input.addEventListener("keydown", onPhoneKeydown)
        input.addEventListener("paste", onPhonePaste)
    }

});

const filterBox = document.querySelectorAll('.fleet__item');

document.getElementById('range').addEventListener('change', function () {

    let filterClass = this.value

    filterBox.forEach(elem => {
        elem.classList.remove('hide');
        if (!elem.classList.contains(filterClass) && filterClass !== 'all') {
            elem.classList.add('hide');
        }
    });
});

document.getElementById('passengers').addEventListener('change', function () {

    let filterClass = this.value

    filterBox.forEach(elem => {
        elem.classList.remove('hide-p');
        if (!elem.classList.contains(filterClass) && filterClass !== 'all') {
            elem.classList.add('hide-p');
        }
    });
});
document.getElementById('purpose').addEventListener('change', function () {

    let filterClass = this.value

    filterBox.forEach(elem => {
        elem.classList.remove('hide-purpose');
        if (!elem.classList.contains(filterClass) && filterClass !== 'all') {
            elem.classList.add('hide-purpose');
        }
    });
});




// document.querySelector('jq-selectbox__dropdown').addEventListener('click', (event) => {

//     if (event.target.tagName !== 'LI') return false;
//     let filterClass = event.target.dataset['f'];

//     filterBox.forEach(elem => {
//         elem.classList.remove('hide');
//         if (!elem.classList.contains(filterClass) && filterClass !== 'all') {
//             elem.classList.add('hide');
//         }
//     });

// });

