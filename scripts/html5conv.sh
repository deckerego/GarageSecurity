#!/bin/sh

EVENT_NAME="$1"
FILE_NAME="$2"
PIXELS="$3"
TIME_EPOCH="$4"
EVENT_NUMBER="$5"

FILE_DIR=$(dirname "$FILE_PATH")
FILE_NAME=$(basename "$FILE_PATH")
FILE_BASE="${FILE_NAME%.*}"

avconv -i "$FILE_PATH" -vcodec h264 -acodec aac -strict -2 "$FILE_DIR/$FILE_BASE.mp4"
rm -r -f "$FILE_PATH"
