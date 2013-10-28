#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

os.chdir(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

import wiringpi
import time
from config import configuration
from bottle import Bottle, get, post, request, template

application = Bottle()

@application.get('/')
def show_status():
    return template('index')

@application.post('/<station_id:int>/command/<command_id:int>')
def execute_command(station_id, command_id):
	# TODO Currently we ignore the station, it's here to support multiple instances in the future
	io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
	io.pinMode(17, io.OUTPUT)
	io.digitalWrite(17, io.HIGH)

	time.sleep(1)
	io.digitalWrite(17, io.LOW)

	show_status()

