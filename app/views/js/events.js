function executeCommand() {
  if(window.confirm("Open/Close Garage Door?")) {
    var request = new XMLHttpRequest();
    request.open("PUT", "remote/0", true);
    request.send();
  }
}

function lightSwitch(buttonTag) {
  var request = new XMLHttpRequest();
  request.open("PUT", "light/0", true);
  request.send();
  lightStatus(buttonTag);
}

function lightStatus(buttonTag) {
  var request = new XMLHttpRequest();
  request.open("GET", "light/0", true);

  request.onload = function(evt) {
    var response = JSON.parse(request.responseText);
    document.getElementById(buttonTag).innerHTML = response.enabled ? "Lights Off" : "Lights On";
  };

  request.send();
}

function silenceStatus(buttonTag) {
  var request = new XMLHttpRequest();
  request.open("GET", "alerts", true);

  request.onload = function(evt) {
    var response = JSON.parse(request.responseText);
    document.getElementById(buttonTag).innerHTML = response.silence ? "Enable Alerts" : "Silence Alerts";
  };

  request.send();
}

function lastEvent(propTag) {
  var request = new XMLHttpRequest();
  request.open("GET", "lastevent", true);

  request.onload = function(evt) {
    var response = JSON.parse(request.responseText);
    document.getElementById(propTag).innerHTML = response.datetime
  };

  request.send();
}

function toggleSilence(buttonTag) {
  var request = new XMLHttpRequest();
  request.open("GET", "alerts", true);

  request.onload = function(evt) {
    var response = JSON.parse(request.responseText);

    var put = new XMLHttpRequest();
    put.open("PUT", "alerts", false);
    put.setRequestHeader('Content-Type', 'application/json');
    put.send(JSON.stringify({ silence: ! response.silence }));

    document.getElementById(buttonTag).innerHTML = response.silence ? "Silence Alerts" : "Enable Alerts";
  };

  request.send();
}

function loadThermals(tempTag, humidTag) {
  var request = new XMLHttpRequest();
  request.open("GET", "environment", true);

  request.onload = function(evt) {
    var response = JSON.parse(request.responseText);
    var temperature = response.fahrenheit == null ? "NA" : response.fahrenheit.toFixed(2) + " &deg;F";
    var humidity = response.relative_humidity == null ? "NA" : response.relative_humidity.toFixed(2) + "%";

    document.getElementById(tempTag).innerHTML = temperature;
    document.getElementById(humidTag).innerHTML = humidity;
  };

  request.send();
}
