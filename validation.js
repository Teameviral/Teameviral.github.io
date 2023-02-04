document.getElementById("menu-toggle").addEventListener("click", function() {
  var menu = document.querySelector("header nav ul");
  if (menu.style.display === "flex") {
    menu.style.display = "none";
  } else {
    menu.style.display = "flex";
  }
});
