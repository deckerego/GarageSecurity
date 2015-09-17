#!/bin/bash

API_URL="http://localhost/door/$1"
API_USER="pi"
API_PASS=
FILE_PATH="$2"
PIXELS="$3"
TIME_EPOCH="$4"
EVENT_NUMBER="$5"
FILE_DIR=$(dirname "$FILE_PATH")

chmod g+w "$FILE_DIR"

PUT=`sed 's|MOTION_FILE_NAME|'$FILE_PATH'|g' </usr/local/motion/motion.json`
PUT=`echo $PUT | sed s/MOTION_PIXELS_DETECTED/$PIXELS/`
PUT=`echo $PUT | sed s/MOTION_SECONDS_SINCE_EPOCH/$TIME_EPOCH/`
PUT=`echo $PUT | sed s/MOTION_EVENT_NUMBER/$EVENT_NUMBER/`

curl -u "$API_USER:$API_PASS" -H "Content-Type: application/json" -XPUT -d "$PUT" "$API_URL"
