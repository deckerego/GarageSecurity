<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="css/base.css" type="text/css" />
		<link rel="stylesheet" href="css/layout.css" type="text/css" />
		<link rel="stylesheet" href="css/skeleton.css" type="text/css" />
		<script type="text/javascript" src="js/mjpeg_viewer.js"></script>
		<script type="text/javascript">
			function executeCommand() {
				var request = new XMLHttpRequest();
				request.open("PUT", "remote/0", true);
				request.send()
			}
		</script>
	</head>

	<body>
		<canvas id="camera0" width="1280" height="720"></canvas>
		<br clear="all" />
		<button onClick="executeCommand();">Open or Close Door</button>

		<script type="text/javascript">
			renderCamera("camera0", "/camera0");
		</script>
	</body>
</html>