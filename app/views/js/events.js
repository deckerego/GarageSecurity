function executeCommand() {
  if(window.confirm("Open/Close Garage Door?")) {
    var request = new XMLHttpRequest();
    request.open("PUT", "remote/0", true);
    request.send();
  }
}

function silenceStatus(buttonTag) {
  var request = new XMLHttpRequest();
  request.open("GET", "/alerts", true);

  request.onload = function(evt) {
    var response = JSON.parse(request.responseText);
    document.getElementById(buttonTag).innerHTML = response.silence ? "Enable Alerts" : "Silence Alerts";
  };

  request.send();
}

function toggleSilence(buttonTag) {
  var request = new XMLHttpRequest();
  request.open("GET", "/alerts", true);

  request.onload = function(evt) {
    var response = JSON.parse(request.responseText);

    var put = new XMLHttpRequest();
    put.open("PUT", "/alerts", ! response.silence);
    put.setRequestHeader('Content-Type', 'application/json');
    put.send(JSON.stringify({ silence: true }));

    document.getElementById(buttonTag).innerHTML = response.silence ? "Silence Alerts" : "Enable Alerts";
  };

  request.send();
}

function loadThermals(tempTag, humidTag) {
  var request = new XMLHttpRequest();
  request.open("GET", "/environment", true);

  request.onload = function(evt) {
    var response = JSON.parse(request.responseText);
    document.getElementById(tempTag).innerHTML = response.fahrenheit.toFixed(2) + " &deg;F";
    document.getElementById(humidTag).innerHTML = response.relative_humidity.toFixed(2) + "%";
  };

  request.send();
}
