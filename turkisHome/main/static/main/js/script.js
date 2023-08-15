$(document).ready(function() {
    $('.slider').slick({
        arrows: false,
        autoplay: true,
        autoplaySpeed: 2000,
        infinite: true,
        speed: 500,
        fade: true,
        cssEase: 'linear',
    });

})

$(document).ready(function() {
    $('.slider_main').slick({
        infinite: true,
        speed: 500,
        fade: true,
        cssEase: 'linear',
        appendArrows: $('.arrows'),
        prevArrow: '<button type = "button" class = "slick-prev"></ button>',
        nextArrow: '<button type = "button" class = "slick-next"></ button>'
    });

})

$(document).ready(function() {
    $('.slider_com').slick({
        arrows: false,
        autoplay: true,
        autoplaySpeed: 2000,
        infinite: true,
        speed: 500,
        fade: true,
        cssEase: 'linear'
    });

})

$(document).ready(function() {
    $('.slider_main_com').slick({
        infinite: true,
        speed: 500,
        fade: true,
        cssEase: 'linear',
        appendArrows: $('.arrows_com'),
        prevArrow: '<button type = "button" class = "slick-prev"></ button>',
        nextArrow: '<button type = "button" class = "slick-next"></ button>'
    });

})

$(document).ready(function() {
    $('.slider_cars').slick({
        arrows: false,
        infinite: true,
        fade: true,
        cssEase: 'linear'

    });

})

$(document).ready(function() {
    $('.slider_main_cars').slick({
        infinite: true,
        fade: true,
        cssEase: 'linear',
        appendArrows: $('.arrows_car'),
        prevArrow: '<button type = "button" class = "slick-prev"></ button>',
        nextArrow: '<button type = "button" class = "slick-next"></ button>'
    });
})

function menuFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {

    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}