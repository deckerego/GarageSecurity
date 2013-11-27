#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from routes import application
from bottle import run

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 9003))
	run(application, reloader = False, host = '0.0.0.0', port = port)
	application.close()
