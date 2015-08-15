#!/bin/bash

if [[ -z $1 ]]; then
  echo "Usage: $0 [HOST]"
  exit -1
fi

DEST_HOST=$1

rsync -ave ssh --delete --exclude 'config.py' --exclude '*.pyc' app/ pi@$DEST_HOST:/srv/app/
