#TODO I2C controls for temp/humidity
import inspect
import logging
from config import configuration

logger = logging.getLogger('basemon')

class Temperature(object):
    name = 'temperature'
    keyword = 'temperature'

    def __init__(self):
        super(Temperature, self).__init__()
        self.start()

    def __del__(self):
        self.close()

    # This is invoked when installed as a Bottle plugin
    def setup(self, app):
        self.routes = app

        for other in app.plugins:
            if not isinstance(other, Temperature):
                continue
            if other.keyword == self.keyword:
                raise PluginError("Found another instance of Temperature running!")

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
        logger.info("Closing Temperature Connection")
        
    def start(self):
        logger.info("Opening Temperature Connection")

    def get_temperature(self):
        return -1

    def get_humidity(self):
        return -1

class PluginError(Exception):
    pass

Plugin = Temperature