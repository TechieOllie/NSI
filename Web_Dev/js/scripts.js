window.onload = function () {
  document.getElementById("loading-screen").style.display = "none";
};

var flash = document.getElementById("flash");

setInterval(function () {
  if (flash.style.color === "red") {
    flash.style.color = "white";
  } else {
    flash.style.color = "red";
  }
}, 200);

var viewportWidth = window.innerWidth;
var viewportHeight = window.innerHeight;

var img = document.getElementById("img-nantes");
img.style.width = viewportWidth * 0.6 + "px";
img.style.height = viewportHeight * 0.6 + "px";
