#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from config import configuration

class Camera():

  def __init__(self):
    self.top_level_url = 'http://localhost:8081'
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, self.top_level_url, "user", "pass")
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)

  def get_image(self):
    response = urllib2.urlopen(self.top_level_url)

    content_type = response.headers.get('Content-Type')
    boundary = content_type.split(';')[1].split('=')[1]

    # Seek ahead to boundary
    line = response.readline()
    while line.strip() != boundary:
        line = reponse.readline()

    # Read chunk
    while line.strip() != '':
        parts = line.split(':')
        if len(parts) > 1 and parts[0] == 'Content-Length':
            chunk_length = int(parts[1].strip())
        line = response.readline()

    return response.read(chunk_length)
