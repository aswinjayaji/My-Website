//
$(document).ready(function() {
    $('#fullpage').fullpage({
        'verticalCentered': false,
        'scrollingSpeed': 600,
        'autoScrolling': true,
        'css3': true,
        'navigation': true,
        'navigationPosition': 'right',
    });
});

// wow
$(function() {
    new WOW().init();
    $(".rotate").textrotator();
})