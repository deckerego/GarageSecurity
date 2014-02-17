var CurrentRange = 0;

function renderCamera(canvasId, imageUrl, rangeUrl) {
  var canvas = document.getElementById(canvasId);
  var context = canvas.getContext('2d');

  //Start the event loop for fetching the rangefinder distance
  getRange(rangeUrl)

  //Start the render loop for showing the HUD
  var image = new Image();
  image.src = imageUrl

  function drawFrame() {
  	//Draw the JPEG image from the camera
    context.drawImage(image, 0, 0, canvas.width, canvas.height);

    //Set the font style for overdraw
    context.font = "12px sans-serif";
	context.fillStyle = 'white';

	//Overdraw HUD
	printDate(canvas, new Date())
    printRange(canvas);

	//Redraw
    window.requestAnimationFrame(drawFrame);
  }

  drawFrame();
}

function printDate(canvas, date) {
	var context = canvas.getContext('2d');
	context.textAlign = "right";
	context.textBaseline = "bottom";
	context.fillText(date.toISOString(), canvas.width, canvas.height);
}

function printRange(canvas) {
  	var context = canvas.getContext('2d');
	context.textAlign = "left";
	context.textBaseline = "bottom";
	context.fillText("Range: " + CurrentRange, 0, canvas.height);    
}

function getRange(rangeUrl) {
	var request = new XMLHttpRequest();
	request.open("GET", rangeUrl, true);
	request.onload = function(evt) {
		response = JSON.parse(request.responseText);
		CurrentRange = response.distance;
		getRange(rangeUrl)
	};
	request.send();
}