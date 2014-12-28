<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="css/styles.css" type="text/css" />
		<script type="text/javascript" src="js/mjpeg_viewer.js"></script>
		<script type="text/javascript">
			function executeCommand() {
				if(window.confirm("Open/Close Garage Door?")) {
					var request = new XMLHttpRequest();
					request.open("PUT", "remote/0", true);
					request.send()
				}
			}

			function loadThermals(tempTag, humidTag) {
				var request = new XMLHttpRequest();
				request.open("GET", "/environment", true);

				request.onload = function(evt) {
					var response = JSON.parse(request.responseText);
					document.getElementById(tempTag).innerHTML = response.fahrenheit.toFixed(2) + " &deg;F"
					document.getElementById(humidTag).innerHTML = response.relative_humidity.toFixed(2) + "%"
				};

				request.send();
			}
		</script>
	</head>

	<body>

		<span class="wrapper">
			<span class="container">
				<span class="canvas-container">
					<canvas id="camera0" width="1280" height="720"></canvas>
				</span>
			</span>

			<table class="prop_overlay" id="therm_props">
				<tr><td>Temperature:</td> <td id="temperature" /></tr>
				<tr><td>Humidity:</td> <td id="humidity" /></tr>
			</table>

			<button id="openDoor" onClick="executeCommand();">Open or Close Door</button>
			<button id="archives" onClick="window.location.assign('/media/');">Video Archives</button>
			<button id="system" onClick="window.location.assign('/monit/');">System Stats</button>

		</span>

		<script type="text/javascript">
			loadThermals("temperature", "humidity")
			renderCamera("camera0", "{{webcam_url}}");
		</script>
	</body>
</html>
