#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging

logging.basicConfig(level=logging.WARN, format='%(levelname)-8s %(message)s')

os.chdir(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

import json
import time
import datetime
from rangefinder import Rangefinder
from temperature import Temperature
from jabber import Jabber
from config import configuration
from bottle import Bottle, response, HTTPResponse, static_file, get, put, request, template

temperature = Temperature()
rangefinder = Rangefinder()
jabber = Jabber(configuration.get('xmpp_username'), configuration.get('xmpp_password'))

application = Bottle()
application.install(temperature)
application.install(rangefinder)
application.install(jabber)

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

@application.post('/environment')
def alert_motion(temperature):
	return '{ "farenheit": -1, "humidity": -1 }'

@application.get('/pumpwell')
def show_image(rangefinder):
	return '{"distance": %d}' % rangefinder.get_range()
