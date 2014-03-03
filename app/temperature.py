#TODO I2C controls for temp/humidity
import inspect
import logging
import smbus
import time
from config import configuration

logger = logging.getLogger('basemon')

class Temperature(object):
    name = 'temperature'
    keyword = 'temperature'

    def __init__(self):
        super(Temperature, self).__init__()
        self.bus = smbus.SMBus(1)
        self.address = 0x27
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

    def get_conditions(self):
        self.bus.write_quick(self.address)
        time.sleep(0.1)

        Hum_H = self.bus.read_byte(self.address);
        Hum_L = self.bus.read_byte(self.address);
        Temp_H = self.bus.read_byte(self.address);
        Temp_L = self.bus.read_byte(self.address);

        status = (Hum_H >> 6) & 0x03;
        Hum_H = Hum_H & 0x3f;
        H_dat = (Hum_H << 8) | Hum_L;
        T_dat = (Temp_H << 8) | Temp_L;
        T_dat = T_dat / 4;

        # TODO precalculate these constants rather than just typing them out
        humidity = H_dat * 0.0061
        celsius = (T_dat * 0.01007) - 40.0
        farenheit = ((celsius * 9) / 5) + 32

        return (humidity, farenheit, status)

class PluginError(Exception):
    pass

Plugin = Temperature