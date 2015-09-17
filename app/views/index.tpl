<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="installed/bootstrap/dist/css/bootstrap.min.css">
		<link rel="stylesheet" href="installed/bootstrap/dist/css/bootstrap-theme.min.css">
		<link rel="stylesheet" href="css/styles.css" type="text/css">
	</head>

	<body>
		<nav class="navbar navbar-default">
			<div class="container-fluid">
				<ul class="nav navbar-nav">
					<li><a class="navbar-brand" href="/">Home</a></li>
					<li><button type="button" id="openDoor" class="btn btn-default navbar-btn" onClick="executeCommand();">Open or Close Door</button></li>
					<li><button type="button" id="silent" class="btn btn-default navbar-btn" onClick="toggleSilence('silent');">(Un)Set Alerts</button></li>
					<li><button type="button" id="archives" class="btn btn-default navbar-btn" onClick="window.location.assign('archive');">Video Archives</button></li>
				</ul>
				<ul class="nav navbar-nav navbar-right">
					<li><p class="navbar-text">Last Event: <span id="lastevent"></span></p></li>
					<li><p class="navbar-text">Temperature: <span id="temperature" /></span></p></li>
					<li><p class="navbar-text">Humidity: <span id="humidity" /></span></p></li>
				</ul>
			</div>
		</nav>

 		<div class="container-fluid">
			<div class="row wrapper">
				<div class="col-lg-12 camera-container">
					<span class="canvas-container">
						<canvas id="camera0" width="1280" height="720"></canvas>
					</span>
				</div>
		  </div>
		</div>

		<script src="installed/jquery/dist/jquery.min.js"></script>
		<script src="installed/bootstrap/dist/js/bootstrap.min.js"></script>
		<script type="text/javascript" src="js/mjpeg_viewer.js"></script>
		<script type="text/javascript" src="js/events.js"></script>
		<script type="text/javascript">
			loadThermals("temperature", "humidity")
			renderCamera("camera0", "{{webcam_url}}");
			silenceStatus("silent");
			lastEvent("lastevent")
		</script>
	</body>
</html>
