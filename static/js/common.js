$(document).ready(function () {
    $(".slider").bxSlider({
        auto: true,
        pasue: 5000,
    });
});

$(function () {
    $(".readmore").on("click", function () {
        $(this).toggleClass("on-click");
        $(".hide-text").slideToggle(1000);
    });
});