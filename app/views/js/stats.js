function getTempHumidity(url, tempId, humidId) {
  var request = new XMLHttpRequest();
  request.open("GET", url, true);

  request.onload = function(evt) {
    response = JSON.parse(request.responseText);

    var farenheit = (response.celsius * 1.8) + 32

    document.getElementById(tempId).innerHTML = farenheit;
    document.getElementById(humidId).innerHTML = response.relative_humidity;
  };

  request.send();
}

function getDetector(url, depthId) {
  var request = new XMLHttpRequest();
  request.open("GET", url, true);

  request.onload = function(evt) {
    response = JSON.parse(request.responseText);
    document.getElementById(depthId).innerHTML = response.detected;
  };

  request.send();
}