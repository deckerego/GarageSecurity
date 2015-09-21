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
					<li class="navbar-brand">/</li>
					<li><a class="navbar-brand" href="home">Camera</a></li>
					<li class="navbar-brand">/</li>
					<li class="navbar-brand">Archive</li>
				</ul>
        <ul class="nav navbar-nav navbar-right">
					<div class="btn-group">
					  <button type="button" class="btn btn-default navbar-btn dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
					    {{date}} <span class="caret"></span>
					  </button>
					  <ul class="dropdown-menu">
					    % for archive_date in dates:
								<li><a href="?date={{archive_date}}">{{archive_date}}</a></li>
							% end
					  </ul>
					</div>
        </ul>
			</div>
		</nav>

 		<div class="container-fluid">
      <div class="row">
        % for archive_image, archive_video in images:
          <div class="col-xs-6 col-md-4">
            <a href="video?date={{date}}&vid={{archive_video}}" class="thumbnail">
              <img src="/media/{{date}}/{{archive_image}}">
            </a>
          </div>
        % end
      </div>
    </div>

		<script src="installed/jquery/dist/jquery.min.js"></script>
		<script src="installed/bootstrap/dist/js/bootstrap.min.js"></script>
	</body>
</html>
