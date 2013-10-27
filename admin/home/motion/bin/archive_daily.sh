#!/bin/bash

YESTERDAY=$(date +%G%m%d --date="@$[`date +%s` - 86400]")
BASE_PATH='/home/motion/garage'
BASE_FILES="$BASE_PATH/*-$YESTERDAY*"
ARCHIVE_PATH="$BASE_PATH/archives"
ARCHIVE_FILE="$ARCHIVE_PATH/$YESTERDAY.tar.xz"

tar cvJf "$ARCHIVE_FILE" $BASE_FILES
