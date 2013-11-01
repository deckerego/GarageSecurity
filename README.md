GarageSecurity
==============

A front-end to the Motion subsystem and Raspberry Pi GPIO, used for remote residential garage surveillance.


Setup
-----

Hardware setup is available at: http://deckerego.blogspot.com/2013/10/your-barn-door-is-open.html

Setting up Ubuntu for the app is detailed at: http://deckerego.blogspot.com/2013/10/your-barn-door-is-off-its-hinges.html


Installation
------------

1. Install python-distribute to obtain Python's easy_install
2. Install pip using easy_install (how meta) for updating application dependencies
3. Install libapache2-mod-wsgi to permit Apache to host Bottle
4. Clone this repository, which includes the Bottle webapp and some admin configs/scripts
5. Install GarageSecurity's dependencies using pip install -r pip_requirements.txt
6. Allow www-data to access the GPIO port using the WiringPi utility

More details are available at http://deckerego.blogspot.com/2013/10/your-barn-door-is-on-display.html
