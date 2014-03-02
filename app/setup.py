#!/usr/bin/env python

from setuptools import setup
import os

setup(
    name='BasementMonitor',
    version='0.1',
    description='A front-end that uses a Raspberry Pi to monitor sump pump well height as well as ambient temperature & humidity, hopefully so your basement does not become an indoor swimming pool.',
    author='DeckerEgo',
    author_email='deckerego@gmail.com',
    url='https://github.com/deckerego/BasementMonitor',
    packages=[''],
    long_description=open('../README.md').read(),
    data_files=[
        ('views',    [os.path.join('views', 'index.tpl')]),
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
        'wiringpi (>=1.0.5)',
        'sleekxmpp (>=1.1.11)',
        'pyserial (>=2.7)'
    ],
	)
