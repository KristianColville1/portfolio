$(document).ready(function () {
    var tooltipTriggerList = [].slice.call(
        document.querySelectorAll('[data-bs-toggle="tooltip"]')
    );
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    /**
     * Dropdowns.
     * Slides dropdown menu's for nice & smooth effect.
     * Improves the UI and makes the website more cohesive.
     */

    // when called slides up any open dropdowns
    let slideAllDropdownsUp = () => {
        $(".dropdown-menu").each(function () {
            $(this).slideUp().removeClass("menu-activated");
        });
    };

    $(".dropdown-toggle").on("click", function (e) {
        e.preventDefault();
        let menu = $(this).next();
        if ($(menu).hasClass("menu-activated")) {
            $(menu).slideUp("slow").removeClass("menu-activated");
        } else {
            slideAllDropdownsUp(); // before sliding down new menu close others up
            $(menu).slideDown("fast").addClass("menu-activated");
        }
    });

    // if the mouse leaves
    $(".dropdown-menu").on("mouseleave", function (e) {
        e.preventDefault();
        let menu = $(this);
        $(menu).slideUp().removeClass("menu-activated");
    });
})


