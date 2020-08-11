$(document).ready(function() {
    console.log("loaded");
    $material.init();

    $(document).on("submit", "#register-form", function (e) {
        e.preventDefault();
        console.log("form submitted");

    });

});