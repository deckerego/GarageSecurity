#!/bin/bash

echo "A motion event was recorded and is attached." | mutt -s "Garage Security System" -a "$1" -- address@nowhere.egg

