GarageSecurity
==============

A front-end to the Motion subsystem and Raspberry Pi GPIO, used for remote residential garage surveillance.


Setup
-----

Hardware setup is available at: http://blog.deckerego.net/2013/10/your-barn-door-is-open.html

Setting up Ubuntu for the app is detailed at: http://blog.deckerego.net/2013/10/your-barn-door-is-off-its-hinges.html


Installation
------------

1. Install python-distribute to obtain Python's easy_install
2. Install pip using easy_install (how meta) for updating application dependencies
3. Install OpenCV and its Python libraries (see http://docs.opencv.org/doc/tutorials/introduction/table_of_content_introduction/table_of_content_introduction.html)
4. Install libapache2-mod-wsgi to permit Apache to host Bottle
5. Install libapache2-mod-proxy to proxy the MJPEG webcamm feed through Apache
6. Clone this repository or download the .ZIP, which will include the Bottle webapp and some admin configs/scripts
7. Install GarageSecurity's dependencies using pip install -r app/pip_requirements.txt
8. Expose the GPIO port you connect the garage door opener to using the WiringPi GPIO Utility, e.g. gpio export 17 out
9. Allow www-data to access the GPIO port by adding it to the gpio user group in /etc/group
10. Copy the files within the app/ directory into /srv/security
11. Add or modify config files as detailed in the admin/ directory

More details are available at http://blog.deckerego.net/2013/10/your-barn-door-is-on-display.html
