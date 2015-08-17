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

1. Install the base packages with `sudo apt-get install python-distribute python-dev python-smbus libapache2-mod-wsgi libapache2-mod-proxy-html libapache2-mod-authnz-external motion`
2. Install the GPIO userspace tools at https://projects.drogon.net/raspberry-pi/wiringpi/download-and-install/
3. Enable the Apache2 modules using `a2enmod authnz_external proxy_http`
4. Edit `/etc/default/motion` and set it to start on boot
5. Motion may crash on startup due to issues with uv4l - if so use the included `config/etc/init.d/motion` script to replace the default init script, so that it can load necessary compatability libraries
6. Install PIP using `sudo easy_install pip`
7. Clone this repository or download the .ZIP, which will include the Bottle webapp and some admin configs/scripts
8. Install GarageSecurity's dependencies using pip install -r app/requirements.txt
9. Expose the GPIO port you connect the garage door opener to using the WiringPi GPIO Utility, e.g. `gpio export 17 out`. You may want to add this statement to `/etc/rc.local` so that it will be exported at startup.
10. Allow www-data to access the GPIO port by adding it to the gpio user group in /etc/group
11. Allow www-data to access to I2C by adding it to the i2c user group in /etc/group
12. Copy the files within the app/ directory into /srv/app
13. Copy the service config files from config/etc into the appropriate /etc directory, altering them as needed.
14. Copy the alert scripts from the `scripts/` directory into `/usr/local/motion`, modifying `rest_call.sh` so that API_USER and API_PASS are set to your "pi" usernamed and password used to log in to Apache
15. Create a copy of app/config.sample as /srv/app/config.py, altering config.py to fit your preferences
16. Start up (or restart) Apache2

GPIO Permissions Issues
-----------------------
You may find that the GPIO buttons don't work as expected - this may be due to permissions issues within the `/sys/class/gpio/` devices. This can sometimes be fixed by changing `/etc/udev/rules.d/99-com.rules` to have the following gpio rules: `SUBSYSTEM=="gpio*", PROGRAM="/bin/sh -c 'chown -H -R root:gpio /sys/class/gpio/* && chmod -R 770 /sys/class/gpio/*; chown -R root:gpio /sys/devices/virtual/gpio && chmod -R 770 /sys/devices/virtual/gpio'"`
