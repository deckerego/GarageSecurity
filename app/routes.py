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
import camera
from vision import Vision
from jabber import Jabber
from config import configuration
from bottle import Bottle, response, HTTPResponse, static_file, get, put, request, template

jabber_service = Jabber(configuration.get('xmpp_username'), configuration.get('xmpp_password'))
vision_service = Vision(configuration.get('webcam_host'), configuration.get('webcam_port'))

application = Bottle()
#application.install(jabber_service)

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

@application.get('/camera0')
def show_image():
	response.headers['Content-Type'] = 'image/jpeg'
	return camera.get_still()

@application.get('/status')
def show_status():
	return '{ "last_area_detected": %s }' % last_area_detected

@application.get('/door')
def door_status():
	template_image = configuration.get('vision_template_image')
	template_coords = configuration.get('vision_template_coords')
	template_margin = configuration.get('vision_template_margin')
	
	is_closed, location = vision_service.look_if_closed(template_image, template_coords, template_margin)

	return '{ "closed": %s, "location": [%d, %d] }' % (is_closed, location[0], location[1])

@application.put('/picture_save')
def picture_save():
	motion_event = request.json
	date_time = time.localtime(motion_event['event_time'])
	time_string = time.strftime('%a, %d %b %Y %H:%M:%S', date_time)
	image_file_path = motion_event['file']

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

	jabber.send_recipients('Motion in Garage Area Detected at %s' % time_string)

	return request.body.getvalue()

@application.put('/remote/<button:int>')
def push_remote_button(button):
	if gpio.push_button(button):
		return '{ "pressed": %d }' % button
	else:
		raise HTTPResponse('{ "error": %d }' % button, 500)
