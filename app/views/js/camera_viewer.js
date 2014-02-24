function renderCamera(canvasId, sourceUrl) {
  var canvas = document.getElementById(canvasId);
  var context = canvas.getContext('2d');
  var image = new Image();

  function drawFrame() {
    context.drawImage(image, 0, 0, canvas.width, canvas.height);

    //Set the font style for overdraw
    context.font = "12px sans-serif";
    context.fillStyle = 'white';

    //Overdraw HUD
    printDate(canvas, new Date())

    image = new Image();
    image.src = sourceUrl
    image.onload = drawFrame;
  }

  drawFrame();
}

function printDate(canvas, date) {
	var context = canvas.getContext('2d');
	context.textAlign = "right";
	context.textBaseline = "bottom";
	context.fillText(date.toISOString(), canvas.width, canvas.height);
}