#!/bin/sh

curl -v -H "Content-Type: application/json" -X PUT -d @picture_save.json http://localhost:9003/picture_save