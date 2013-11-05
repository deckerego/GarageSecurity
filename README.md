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
4. Install libapache2-mod-proxy to proxy the MJPEG webcamm feed through Apache
5. Clone this repository or download the .ZIP, which will include the Bottle webapp and some admin configs/scripts
6. Install GarageSecurity's dependencies using pip install -r pip_requirements.txt
7. Expose the GPIO port you connect the garage door opener to using the WiringPi GPIO Utility, e.g. gpio export 17 out
8. Allow www-data to access the GPIO port by adding it to the gpio user group in /etc/group
9. Copy the Python (.py) and view (view/) files into /srv/security
10. Add or modify config files as detailed in the admin/ directory

More details are available at http://deckerego.blogspot.com/2013/10/your-barn-door-is-on-display.html
