#!/bin/sh

curl -v -H "Content-Type: application/json" -X PUT -d @area_detected.json http://localhost:9003/area_detected