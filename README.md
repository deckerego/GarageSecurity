GarageSecurity
==============

A web interface for remote residential garage surveillance. This uses a Raspberry Pi to connect to a universal garage door opener via GPIO, a Maxbotix ultrasonic range finder and a Raspberry NoIR video camera. 

Hardware
--------

<table>
  <tr>
    <td>Raspberry Pi Model B</td>
    <td>https://www.sparkfun.com/products/11546</td>
  </tr>
  <tr>
    <td>Raspberry Pi NoIR Camera</td>
    <td>https://www.sparkfun.com/products/12654</td>
  </tr>
  <tr>
    <td>Chamberlain Universal Garage Remote</td>
    <td>http://www.chamberlain.com/clicker-and-accessories/universal-clicker-products/clicker-universal-remote-control</td>
  </tr>
  <tr>
    <td>XL-Maxsonar EZ4</td>
    <td>http://www.maxbotix.com/documents/XL-MaxSonar-EZ_Datasheet.pdf</td>
  </tr>
  <tr>
    <td>Resistors, NPN transistors, NPN MOSFET</td>
    <td>Available at Sparkfun, Adafruit, Radio Shack or from de-soldering unused electronics.</td>
  </tr>
</table>

Setup
-----

The hardware setup for the garage door remote is available at: http://blog.deckerego.net/2013/10/your-barn-door-is-open.html . Setup for the XL-Maxsonar will be posted shortly.

Setting up Ubuntu for the app is detailed at: http://blog.deckerego.net/2013/10/your-barn-door-is-off-its-hinges.html


Installation
------------

1. Install python-distribute to obtain Python's easy_install
2. Install pip using easy_install (how meta) for updating application dependencies
4. Install libapache2-mod-wsgi to permit Apache to host Bottle
5. Install libapache2-mod-proxy to proxy the MJPEG webcam feed through Apache
6. Clone this repository or download the .ZIP, which will include the Bottle webapp and some admin configs/scripts
7. Install libjpeg-dev
  1. sudo apt-get install libjpeg-dev
  2. sudo ln -s /usr/lib/arm-linux-gnueabihf/libz.so /usr/lib/libz.so
  3. sudo ln -s /usr/lib/arm-linux-gnueabihf/libjpeg.so /usr/lib/libjpeg.so
  4. sudo ln -s /usr/lib/arm-linux-gnueabihf/libfreetype.so /usr/lib/libfreetype.so
8. Install GarageSecurity's dependencies using pip install -r app/pip_requirements.txt
9. Expose the GPIO port you connect the garage door opener to using the WiringPi GPIO Utility, e.g. gpio export 17 out
10. Allow www-data to access the GPIO port by adding it to the gpio user group in /etc/group
11. Allow www-data to access the Raspberry Pi camera by adding it to the video user group in /etc/group
12. Copy the files within the app/ directory into /srv/security
13. Add or modify config files as detailed in the admin/ directory

More details are available at http://blog.deckerego.net/search/label/garage%20door