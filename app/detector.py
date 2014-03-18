import inspect
import logging
import wiringpi
from config import configuration

logger = logging.getLogger('basemon')

class Detector(object):
    name = 'detector'
    keyword = 'detector'
    detector_pin = 17


    def __init__(self):
        super(Detector, self).__init__()
        self.gpio = None
        self.start()

    def __del__(self):
        self.close()

    # This is invoked when installed as a Bottle plugin
    def setup(self, app):
        self.routes = app

        for other in app.plugins:
            if not isinstance(other, Detector):
                continue
            if other.keyword == self.keyword:
                raise PluginError("Found another instance of Detector running!")

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
        logger.info("Closing Detector Connection")
        
    def start(self):
        logger.info("Opening Detector Connection")
        self.gpio = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
        self.gpio.pinMode(self.detector_pin, self.gpio.INPUT)        

    def detection(self):
        return self.gpio.digitalRead(self.detector_pin) != 1

class PluginError(Exception):
    pass

Plugin = Detector