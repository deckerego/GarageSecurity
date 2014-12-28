#!/bin/bash

if [[ -z $1 ]]; then
  echo "Usage: $0 [HOST]"
  exit -1
fi

DEST_HOST=$1

rsync -ave ssh --delete --exclude 'config.py' --exclude '*.pyc' app/ pi@$DEST_HOST:/srv/app/
#rsync -ave ssh --delete scripts/ pi@$DEST_HOST:/usr/local/motion/
#rsync -ave ssh config/etc/apache2/sites-available/security pi@$DEST_HOST:/etc/apache2/sites-available/security
