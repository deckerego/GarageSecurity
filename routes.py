#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

os.chdir(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from config import configuration
from bottle import Bottle, error, template

application = Bottle()

@Bottle.error(application)
def error(error):
	return '{ "error": "%s" }' % 'An unexpected error has occurred'

@application.get('/')
def show_status():
    return template('index')
