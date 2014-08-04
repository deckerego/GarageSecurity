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
