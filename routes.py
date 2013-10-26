#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

os.chdir(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

import RPi.GPIO as GPIO
import time
from config import configuration
from bottle import Bottle, error, template

application = Bottle()

@Bottle.error(application)
def error(error):
	return '{ "error": "%s" }' % 'An unexpected error has occurred'

@application.get('/')
def show_status():
    return template('index')

@application.post('/<door_idx:int>/door')
def fire_remote(door_idx):
	# TODO Currently we ignore the door index, it's here to support multiple doors in the future
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)

	GPIO.output(11, GPIO.HIGH)
	time.sleep(0.05)
	GPIO.output(11, GPIO.LOW)

	GPIO.cleanup()

	return template('index')
