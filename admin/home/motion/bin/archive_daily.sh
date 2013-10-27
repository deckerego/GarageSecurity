#!/bin/bash

DATE=$(date +%G%m%d --date="@$[`date +%s` - 86400]")
ARCH_PATH='/srv/motion'

mkdir $ARCH_PATH/$DATE
mv $ARCH_PATH/*-$DATE* /$ARCH_PATH/$DATE
