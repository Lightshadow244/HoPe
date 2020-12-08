var slideIndex = 0;
showSlides();

function showSlides() {
  console.log("test")
  var i;
  var slides = document.getElementsByClassName("hope-slideshow-slide");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}
  slides[slideIndex-1].style.display = "block";

  setTimeout(showSlides, 2000); // Change image every 2 seconds
}
