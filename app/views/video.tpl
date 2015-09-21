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
				<ul class="nav navbar-nav navbar-right">
					<li><a class="navbar-brand glyphicon glyphicon-remove" aria-hidden="true" href="archive?date={{date}}"></a></li>
        </ul>
      </div>
    </nav>

 		<div class="container-fluid">
      <div class="well well-lg">
        <ul class="pager">
          <li>
            <video controls>
              <source src="/media/{{date}}/{{archive_video}}" type="video/mp4">
            </video>
          </li>
        </ul>
      </div>
    </div>

		<script src="installed/jquery/dist/jquery.min.js"></script>
		<script src="installed/bootstrap/dist/js/bootstrap.min.js"></script>
	</body>
</html>
