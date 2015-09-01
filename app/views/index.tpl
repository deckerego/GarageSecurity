<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="installed/bootstrap/dist/css/bootstrap.min.css">
		<link rel="stylesheet" href="installed/bootstrap/dist/css/bootstrap-theme.min.css">
		<link rel="stylesheet" href="css/styles.css?v=101" type="text/css" />
	</head>

	<body>
		<div class="container-fluid">
			<div class="row">
	      <div class="col-sm-4">Last Event: <span id="lastevent"></span></div>
	      <div class="col-sm-4">Temperature: <span id="temperature" /></span></div>
				<div class="col-sm-4">Humidity: <span id="humidity" /></span></div>
			</div>

			<div class="row wrapper">
				<div class="col-lg-12 camera-container">
					<span class="canvas-container">
						<canvas id="camera0" width="1280" height="720"></canvas>
					</span>
				</div>
		  </div>

			<div class="row">
				<div class="col-md-2">
					<button type="button" id="openDoor" class="btn btn-lg btn-default" onClick="executeCommand();">Open or Close Door</button>
				</div>
				<div class="col-md-2">
					<button type="button" id="silent" class="btn btn-lg btn-default" onClick="toggleSilence('silent');">(Un)Set Alerts</button>
				</div>
				<div class="col-md-2">
					<button type="button" id="archives" class="btn btn-lg btn-default" onClick="window.location.assign('/media/');">Video Archives</button>
				</div>
				<div class="col-md-6">
				</div>
			</div>
		</div>

		<script src="installed/jquery/dist/jquery.min.js"></script>
		<script src="installed/bootstrap/dist/js/bootstrap.min.js"></script>
		<script type="text/javascript" src="js/mjpeg_viewer.js?v=101"></script>
		<script type="text/javascript" src="js/events.js?v=101"></script>
		<script type="text/javascript">
			loadThermals("temperature", "humidity")
			renderCamera("camera0", "{{webcam_url}}");
			silenceStatus("silent");
			lastEvent("lastevent")
		</script>
	</body>
</html>
