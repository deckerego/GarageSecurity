#!/bin/bash

FILE_DESC=$(ls -s "$1")
FILE_SIZE=${FILE_DESC% *}

if [[ $FILE_SIZE > 600 ]]; then
    echo "A motion event was recorded and is attached." | mutt -s "Garage Security System" -a "$1" -- deckerego@gmail.com
fi

