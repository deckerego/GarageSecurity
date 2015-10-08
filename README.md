GarageSecurity
==============

A web interface for remote residential garage surveillance. This uses a Raspberry Pi to connect to a universal garage door opener via GPIO and a webcam or Raspberry NoIR video camera.

Hardware Punch List
-------------------

<table>
  <tr>
    <td>Raspberry Pi (works with all models)</td>
    <td>https://www.adafruit.com/product/2266</td>
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
  <tr>
    <td>Optional: Honeywell Temperature and Humidity Sensor</td>
    <td>https://www.sparkfun.com/products/11295</td>
  </tr>
</table>

Security & OS Setup
-------------------

Ensure you install necessary updates and install a firewall (such as UFW) before proceeding. Rather than exposing motion and other services externally, we will be proxying them through Apache.

Especially for the Raspberry Pi camera, I would recommend installing the User space Video4Linux. Instructions for installation are available at http://www.linux-projects.org/modules/sections/index.php?op=viewarticle&artid=14

It may be a good idea to create a crontab entry to delete old captured videos, e.g. `0 1 * * * find /home/motion -ctime +14 -delete`

To enable I2C communication for temperature and humidity monitoring, follow the I2C instructions from Adafruit available at https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

Hardware Installation
---------------------

See http://hackaday.io/project/2049/instructions for hardware installation

Software Installation
---------------------

These installation instructions have been tested with the latest version of Raspian (Jessie)

1. Install the base packages with `sudo apt-get install wiringpi python-dev python-smbus python-imaging apache2 libapache2-mod-proxy-html libapache2-mod-authnz-external motion nodejs-legacy npm monit`
2. Install Bower using `sudo npm install -g bower`
3. Enable the Apache2 modules using `sudo a2enmod authnz_external proxy_http`
4. If you are using the Raspberry Pi camera, add `bcm2835-v4l2` to /etc/modules
5. Edit `/etc/default/motion` and set it to start on boot
6. Clone this repository or download https://github.com/deckerego/GarageSecurity/archive/master.zip which will include the Bottle webapp and some admin configs/scripts
7. Install GarageSecurity's dependencies using `sudo pip install -r app/requirements.txt`
8. Expose the GPIO port you connect the garage door opener to using the WiringPi GPIO Utility, e.g. `gpio export 17 out`. You may want to add this statement to `/etc/rc.local` so that it will be exported at startup.
9. Allow the pi user to access motion files by adding it to the `motion` user group in /etc/group
10. Copy the files within the app/ directory into /srv/garagesec
11. Change into the /srv/garagesec/views directory and execute `bower install bootstrap`
12. Copy the service config files from config/etc into the appropriate /etc directory, altering them as needed.
13. Copy the alert scripts from the `scripts/` directory into `/usr/local/motion`, modifying `rest_call.sh` so that API_USER and API_PASS are set to your "pi" usernamed and password used to log in to Apache
14. Create a copy of app/config.sample as /srv/garagesec/config.py, altering config.py to fit your preferences
15. Start up (or restart) Apache2
16. Ensure config/etc/init.d/garagesec has been copied to /etc/init.d, then install it using `sudo update-rc.d garagesec defaults`
17. Start the webapp using `sudo service garagesec start`


GPIO Permissions Issues
-----------------------
You may find that the GPIO buttons don't work as expected - this may be due to permissions issues within the `/sys/class/gpio/` devices. This can sometimes be fixed by changing `/etc/udev/rules.d/99-com.rules` to have the following gpio rules: `SUBSYSTEM=="gpio*", PROGRAM="/bin/sh -c 'chown -H -R root:gpio /sys/class/gpio/* && chmod -R 770 /sys/class/gpio/*; chown -R root:gpio /sys/devices/virtual/gpio && chmod -R 770 /sys/devices/virtual/gpio'"`
