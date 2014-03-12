<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<link rel="stylesheet" href="css/styles.css" type="text/css" />
		<script type="text/javascript" src="js/stats.js?version=1"></script>
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
				<td>Well Depth:</td>
				<td><span id="depth"></span> cm</td>
			</tr>
		</table>

		<script type="text/javascript">
			getTempHumidity('/environment', 'temperature', 'humidity')
			getDepth('/pumpwell', 'depth')
		</script>
	</body>
</html>
