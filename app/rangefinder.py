import serial
import inspect
import logging
from config import configuration

logger = logging.getLogger('basemon')

class Rangefinder(object):
    name = 'rangefinder'
    keyword = 'rangefinder'

    def __init__(self):
        super(Rangefinder, self).__init__()
        self.start()

    def __del__(self):
        self.close()

    # This is invoked when installed as a Bottle plugin
    def setup(self, app):
        self.routes = app

        for other in app.plugins:
            if not isinstance(other, Rangefinder):
                continue
            if other.keyword == self.keyword:
                raise PluginError("Found another instance of Rangefinder running!")

    # This is invoked within Bottle as part of each route when installed
    def apply(self, callback, route):
        args = inspect.getargspec(callback)[0]
        if self.keyword not in args:
            return callback

        def wrapper(*args, **kwargs):
            kwargs[self.keyword] = self
            rv = callback(*args, **kwargs)
            return rv
        return wrapper

    # De-installation from Bottle as a plugin
    def close(self):
        logger.info("Closing Rangefinder Connection")
        
    def start(self):
        logger.info("Opening Rangefinder Connection")
        self.serial_port = serial.Serial(configuration.get('rangefinder_tty'), 9600, timeout=2, bytesize=8, parity='N', stopbits=1)

    def get_range(self):
        if self.serial_port.isOpen()== False:
            self.serial_port.open()
        else:
            pass
        response = self.serial_port.read(5)
        print "Range Finder: %s" % response
        return int(response[1:])

class PluginError(Exception):
    pass

Plugin = Rangefinder