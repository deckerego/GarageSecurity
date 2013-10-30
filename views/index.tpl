<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="css/styles.css" type="text/css" />
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
		<div class="wrapper">
			<div class="container">
				<div class="canvas-container">
					<canvas id="camera0" width="1280" height="720"></canvas>
				</div>
			</div>
		</div>
		
		<button onClick="executeCommand();">Open or Close Door</button>

		<script type="text/javascript">
			renderCamera("camera0", "/camera0");
		</script>
	</body>
</html>
