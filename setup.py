#!/usr/bin/env python

from setuptools import setup
import os

setup(
    name='GarageSecurity',
    version='0.1',
    description='A front-end to the Motion subsystem and Raspberry Pi GPIO, used for remote residential garage surveillance.',
    author='DeckerEgo',
    author_email='deckerego@gmail.com',
    url='https://github.com/deckerego/GarageSecurity',
    packages=[''],
    long_description=open('README.md').read(),
    data_files=[('views', [os.path.join('views', 'index.tpl')])],
    classifiers=[
    	"License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
    	"Programming Language :: Python",
    	"Development Status :: 1 - Planning",
    	"Intended Audience :: End Users/Desktop",
    	"Topic :: Home Automation"
    ],
    keywords='motion security surveillance garage remote raspberrypi',
    requires=[
        'bottle (==0.10.11)'
    ],
	)
