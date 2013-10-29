<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<script type="text/javascript" src="js/mjpeg_viewer.js"></script>
		<script type="text/javascript" type="text/javascript">
			function renderCameras() {
				render('camera0', "http://localhost:8081");
			}
		</script>
	</head>

	<body onload="renderCameras();">
		<canvas id="camera0" width="1280" height="720"></canvas>
	</body>
</html>