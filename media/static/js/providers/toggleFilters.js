function toggleFilters() {
    var x = document.getElementById("filter-form");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

if (document.getElementById("id_is_add_services").checked) {
    alert("checked");
} else {
    alert("You didn't check it! Let me check it for you.");
}

