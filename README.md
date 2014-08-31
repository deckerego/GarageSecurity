GarageSecurity
==============

A web interface for remote residential garage surveillance. This uses a Raspberry Pi to connect to a universal garage door opener via GPIO and a webcam or Raspberry NoIR video camera.

Hardware Punch List
-------------------

<table>
  <tr>
    <td>Raspberry Pi Model B</td>
    <td>https://www.sparkfun.com/products/11546</td>
  </tr>
  <tr>
    <td>Raspberry Pi NoIR Camera (or a spare Video4Linux-compliant webcam)</td>
    <td>https://www.sparkfun.com/products/12654</td>
  </tr>
  <tr>
    <td>Chamberlain Universal Garage Remote</td>
    <td>http://www.chamberlain.com/clicker-and-accessories/universal-clicker-products/clicker-universal-remote-control</td>
  </tr>
  <tr>
    <td>Resistors, NPN transistors, NPN MOSFET</td>
    <td>Available at Sparkfun, Adafruit, Radio Shack or from de-soldering unused electronics.</td>
  </tr>
</table>

Security & OS Setup
-------------------

Debian setup and some basic security pointers are detailed at: http://blog.deckerego.net/2013/10/your-barn-door-is-off-its-hinges.html

Hardware Installation
---------------------

See http://hackaday.io/project/2049/instructions for hardware installation

Software Installation
---------------------

1. sudo apt-get install python-distribute python-dev libapache2-mod-wsgi libapache2-mod-proxy-html
2. sudo easy_install pip
3. Clone this repository or download the .ZIP, which will include the Bottle webapp and some admin configs/scripts
4. Install GarageSecurity's dependencies using pip install -r app/requirements.txt
5. Expose the GPIO port you connect the garage door opener to using the WiringPi GPIO Utility, e.g. gpio export 17 out
6. Allow www-data to access the GPIO port by adding it to the gpio user group in /etc/group
7. Copy the files within the app/ directory into /srv/app
8. Copy the service config files from config/etc into the appropriate /etc directory, altering them as needed
9. Create a copy of app/config.sample as /srv/app/config.py, altering config.py to fit your preferences
10. Start up (or restart) Apache2
