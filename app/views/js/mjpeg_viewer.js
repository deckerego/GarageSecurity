function renderCamera(canvasId, sourceUrl) {
  var canvas = document.getElementById(canvasId);
  var context = canvas.getContext('2d');

  var image = new Image();
  image.src = sourceUrl

  function drawFrame() {
    try {
      context.drawImage(image, 0, 0, canvas.width, canvas.height);
      window.requestAnimationFrame(drawFrame);
    } catch(e) {
      context.font="30px Arial";
      context.textAlign = "center";
	    context.fillText("Webcam Not Available", canvas.width / 2, canvas.height / 2);
    }
  }

  drawFrame();
}
