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

		<table>
			<tr>
				<td colspan="2">
					<div class="wrapper">
						<div class="container">
							<div class="canvas-container">
								<canvas id="camera" width="1280" height="720"></canvas>
							</div>
						</div>
					</div>
				</td>
			</tr>
		
			<tr>
				<td class="buttonCell" rowspan="2"><button onClick="executeCommand();">Open or Close Door</button></td>
				<td class="buttonCell"><button onClick="window.location.assign('/media/');">Video Archives</button></td>
			</tr>
			<tr>
				<td class="buttonCell"><button onClick="window.location.assign('/monit/');">System Stats</button></td>
			</tr>
		</table>

		<script type="text/javascript">
			renderCamera("camera", "/camera", "/range");
		</script>
	</body>
</html>
