<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="css/styles.css" type="text/css" />
		<script type="text/javascript" src="js/stats.js?version=4"></script>
	</head>

	<body>
		<table>
			<tr>
				<td>Temperature:</td>
				<td><span id="temperature"></span> ˚F</td>
			</tr>
			<tr>
				<td>Relative Humidity:</td>
				<td><span id="humidity"></span>%</td>
			</tr>
			<tr>
				<td>Water Alert:</td>
				<td><span id="detected"></span></td>
			</tr>
		</table>

		<script type="text/javascript">
			getTempHumidity('/environment', 'temperature', 'humidity')
			getDetector('/pumpwell', 'detected')
		</script>
	</body>
</html>
