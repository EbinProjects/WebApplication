document.addEventListener("DOMContentLoaded", function() {
    const homeButton = document.getElementById("homeButton");

    if (homeButton) {
        homeButton.addEventListener("click", function(event) {
            event.preventDefault(); // Prevent default navigation
            window.location.replace(homeButton.href); // Replace history with the 'Home' URL
        });
    }
});
