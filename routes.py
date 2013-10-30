#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

os.chdir(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

#import wiringpi
import time
from config import configuration
from bottle import Bottle, HTTPResponse, static_file, get, put, request, template

application = Bottle()

@application.route('/js/<filename:path>')
def send_js(filename):
    return static_file(filename, root='views/js')

@application.route('/css/<filename:path>')
def send_css(filename):
    return static_file(filename, root='views/css')

@application.get('/')
def show_status():
    return template('index')

@application.get('/recordings')
def show_status():
    return template('recordings')

@application.put('/remote/<button:int>')
def push_remote_button(button):
	# TODO Currently we ignore which button is pressed
	'''
	io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
	io.pinMode(17, io.OUTPUT)
	io.digitalWrite(17, io.HIGH)

	time.sleep(1)
	io.digitalWrite(17, io.LOW)
    '''
	raise HTTPResponse('{ "pressed": %d }' % button, 200)
