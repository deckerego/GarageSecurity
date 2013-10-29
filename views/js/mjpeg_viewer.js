function render(canvasId, sourceUrl) {
  var image = new Image();
  image.src = sourceUrl

  var canvas = document.getElementById(canvasId);
  var context = canvas.getContext('2d');

  function drawFrame() {
    context.drawImage(image, 0, 0, canvas.width, canvas.height);
    window.requestAnimationFrame(drawFrame);
  }

  drawFrame();
}
