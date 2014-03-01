#!/usr/bin/env python

from setuptools import setup
import os

setup(
    name='GarageSecurity',
    version='0.1',
    description='A front-end to the Raspberry Pi that uses the NoIR camera & GPIO for remote residential door control.',
    author='DeckerEgo',
    author_email='deckerego@gmail.com',
    url='https://github.com/deckerego/GarageSecurity',
    packages=[''],
    long_description=open('../README.md').read(),
    data_files=[
        ('views',    [os.path.join('views', 'index.tpl')]),
        ('views/js', [os.path.join('views/js', 'camera_viewer.js')]),
        ('views/css',[os.path.join('views/css', 'styles.css')])
    ],
    classifiers=[
    	"License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
    	"Programming Language :: Python",
    	"Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
    	"Topic :: Home Automation"
    ],
    keywords='motion security surveillance garage remote raspberrypi',
    requires=[
        'bottle (==0.10.11)',
        'picamera (>=1.2)',
        'wiringpi (>=1.0.5)',
        'sleekxmpp (>=1.1.11)',
        'pyserial (>=2.7)',
        'boto (>=2.25.0)',
        'PIL (>=1.1.7)'
    ],
	)
