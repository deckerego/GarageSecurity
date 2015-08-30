<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="css/styles.css?v=101" type="text/css" />
		<script type="text/javascript" src="js/mjpeg_viewer.js?v=101"></script>
		<script type="text/javascript" src="js/events.js?v=101"></script>
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
				<tr><td>Last Event:</td> <td id="lastevent" /></tr>
			</table>

			<button id="openDoor" onClick="executeCommand();">Open or Close Door</button>
			<button id="silent" onClick="toggleSilence('silent');">(Un)Set Alerts</button>
			<button id="archives" onClick="window.location.assign('/media/');">Video Archives</button>
		</span>

		<script type="text/javascript">
			loadThermals("temperature", "humidity")
			renderCamera("camera0", "{{webcam_url}}");
			silenceStatus("silent");
			lastEvent("lastevent")
		</script>
	</body>
</html>
