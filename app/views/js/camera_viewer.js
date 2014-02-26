var CurrentDiff = 0;

function renderCamera(canvasId, sourceUrl, diffUrl) {
  var canvas = document.getElementById(canvasId);
  var context = canvas.getContext('2d');
  var image = new Image();

  getDiff(diffUrl)

  function drawFrame() {
    context.drawImage(image, 0, 0, canvas.width, canvas.height);

    //Set the font style for overdraw
    context.font = "12px sans-serif";
    context.fillStyle = 'white';

    //Overdraw HUD
    printDate(canvas, new Date())
    printDiff(canvas, diffUrl)

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

function printDiff(canvas, date) {
  var context = canvas.getContext('2d');
  context.textAlign = "left";
  context.textBaseline = "bottom";
  context.fillText(CurrentDiff, 0, canvas.height);
}

function getDiff(diffUrl) {
  var request = new XMLHttpRequest();
  request.open("GET", diffUrl, true);
  request.onload = function(evt) {
    response = JSON.parse(request.responseText);
    CurrentDiff = response.rms;
    getDiff(diffUrl)
  };
  request.send();
}