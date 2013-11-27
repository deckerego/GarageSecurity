#!/bin/bash

API_URL=http://localhost:9003/area_detected
FILE_NAME="$1"
PIXELS="$2"
TIME_EPOCH="$3"
EVENT_NUMBER="$4"

PUT=`sed s/MOTION_FILE_NAME/$FILE_NAME/ <motion.json`
PUT=`echo $PUT | sed s/MOTION_PIXELS_DETECTED/$PIXELS/`
PUT=`echo $PUT | sed s/MOTION_SECONDS_SINCE_EPOCH/$TIME_EPOCH/`
PUT=`echo $PUT | sed s/MOTION_EVENT_NUMBER/$EVENT_NUMBER/`

curl -v -H "Content-Type: application/json" -X PUT -d "$PUT" "$API_URL"