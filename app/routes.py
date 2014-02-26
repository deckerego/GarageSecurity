#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging

logging.basicConfig(level=logging.WARN, format='%(levelname)-8s %(message)s')

os.chdir(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

import gpio
import json
import time
import datetime
import rangefinder
from camera import Camera
from jabber import Jabber
from config import configuration
from bottle import Bottle, response, HTTPResponse, static_file, get, put, request, template

camera = Camera()
jabber = Jabber(configuration.get('xmpp_username'), configuration.get('xmpp_password'))

application = Bottle()
application.install(camera)
application.install(jabber)

last_area_detected = None

@application.route('/favicon.ico')
def send_favicon():
	return static_file('favicon.ico', root='views/images')

@application.route('/js/<filename:path>')
def send_js(filename):
	return static_file(filename, root='views/js')

@application.route('/css/<filename:path>')
def send_css(filename):
	return static_file(filename, root='views/css')

@application.get('/')
def dashboard():
	return template('index')

@application.get('/camera/image')
def show_image(camera):
	response.headers['Content-Type'] = 'image/jpeg'
	return camera.get_still()

@application.get('/camera/diff')
def show_image(camera):
	return '{"rms": %d}' % camera.get_difference()

@application.put('/remote/<button:int>')
def push_remote_button(button):
	if gpio.push_button(button):
		return '{ "pressed": %d }' % button
	else:
		raise HTTPResponse('{ "error": %d }' % button, 500)
