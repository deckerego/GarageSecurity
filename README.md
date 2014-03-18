BasementMonitor
===============

A web interface for monitoring sump pump well levels, temperature and humidity. This uses a Raspberry Pi to connect to a Honeywell HIH6130 and an external switch. 

Hardware
--------

Hardware setup is described at http://blog.deckerego.net/2014/03/its-basement-not-swimming-pool.html

Build components include:

<table>
  <tr>
    <td>Raspberry Pi Model A</td>
    <td>https://www.sparkfun.com/products/11837</td>
  </tr>
  <tr>
    <td>Honeywell HIH6130 Breakout Board</td>
    <td>https://www.sparkfun.com/products/11295</td>
  </tr>
  <tr>
    <td>A switch that can be triggered when immersed in water</td>
    <td></td>
  </tr>
  <tr>
    <td>Resistors, NPN transistors, NPN MOSFET, wire</td>
    <td>Available at Sparkfun, Adafruit, Radio Shack or from de-soldering unused electronics.</td>
  </tr>
</table>


Installation
------------

1. Install pip (using sudo apt-get install python-pip)
2. Install libapache2-mod-wsgi to permit Apache to host Bottle
3. Install pwauth and enable the authnz_external module (a2enmod authnz_external) to password protect HTTP access
4. Clone this repository or download the .ZIP, which will include the Bottle webapp and some admin configs/scripts
5. Install BasementMonitor's dependencies using pip install -r app/pip_requirements.txt
6. Enable I2C as described at: http://www.raspberry-projects.com/pi/pi-operating-systems/raspbian/io-pins-raspbian/i2c-pins
7. Copy the files within the app/ directory into /srv/monitor
8. Add or modify config files as detailed in the admin/ directory
