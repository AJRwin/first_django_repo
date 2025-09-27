document.addEventListener("DOMContentLoaded", function() {
    const btn = document.getElementById("toggleBtn");
    const content = document.getElementById("content");

    if (btn && content) {  // only run on pages with these elements
        btn.addEventListener("click", () => {
            if (content.style.display === "none") {
                content.style.display = "block";
                btn.textContent = "Show less";
            } else {
                content.style.display = "none";
                btn.textContent = "Read more";
            }
        });
    }
});
