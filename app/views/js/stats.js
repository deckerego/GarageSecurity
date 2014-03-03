function getTempHumidity(url, tempId, humidId) {
  var request = new XMLHttpRequest();
  request.open("GET", url, true);

  request.onload = function(evt) {
    response = JSON.parse(request.responseText);

    var farenheit = ((response.celsius * 9) / 5) + 32

    document.getElementById(tempId).innerHTML = farenheit;
    document.getElementById(humidId).innerHTML = response.relative_humidity;
  };

  request.send();
}

function getDepth(url, depthId) {
  var request = new XMLHttpRequest();
  request.open("GET", url, true);

  request.onload = function(evt) {
    response = JSON.parse(request.responseText);
    document.getElementById(depthId).innerHTML = response.distance;
  };

  request.send();
}