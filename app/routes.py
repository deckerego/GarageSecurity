#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging

logging.basicConfig(level=logging.WARN, format='%(levelname)-8s %(message)s')
logger = logging.getLogger('garagesec')

os.chdir(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

import gpio
import json
import time
import datetime
from jabber import Jabber
from camera import Camera
from temperature import Temperature
from config import configuration
from bottle import Bottle, HTTPResponse, static_file, get, put, request, response, template

instance_name = configuration.get('instance_name')

camera = Camera()
temperature = Temperature()

jabber_service = Jabber(configuration.get('xmpp_username'), configuration.get('xmpp_password'), camera, temperature)

application = Bottle()
application.install(temperature)
application.install(jabber_service)

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
	return template('index', webcam_url=configuration.get('webcam_url'))

@application.get('/status')
def show_status():
	return '{ "last_area_detected": %s }' % last_area_detected

@application.get('/environment')
def get_environment(temperature):
	humidity, celsius, status = temperature.get_conditions()
	return '{ "relative_humidity": %s, "celsius": %s, "fahrenheit": %s, "status": %s }' % (humidity, celsius, ((celsius * 9) / 5) + 32, status)

@application.get('/snapshot')
def show_snapshot():
	response.headers['Content-Type'] = 'image/jpeg'
	return camera.get_image()

@application.put('/picture_save')
def picture_save(jabber):
	motion_event = request.json
	image_file_path = motion_event['file']

	jabber.send_recipients_image(image_file_path)

	return request.body.getvalue()

@application.put('/movie_start')
def movie_start():
	return request.body.getvalue()

@application.put('/movie_end')
def movie_end():
	return request.body.getvalue()

@application.put('/motion_detected')
def motion_detected():
	return request.body.getvalue()

@application.put('/area_detected')
def area_detected(jabber):
	last_area_detected = datetime.datetime.now()

	motion_event = request.json
	date_time = time.localtime(motion_event['event_time'])
	time_string = time.strftime('%a, %d %b %Y %H:%M:%S', date_time)

	jabber.send_recipients_msg('Motion in %s Detected at %s' % (instance_name, time_string))

	return request.body.getvalue()

@application.put('/remote/<button:int>')
def push_remote_button(button):
	if gpio.push_button(button):
		return '{ "pressed": %d }' % button
	else:
		raise HTTPResponse('{ "error": %d }' % button, 500)
