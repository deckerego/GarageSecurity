I2C = True
try:
    import smbus
except ImportError:
	I2C = False

import inspect
import logging
import time
from config import configuration

logger = logging.getLogger('basemon')

class Temperature(object):
    name = 'temperature'
    keyword = 'temperature'
    sensor_max = 16383
    temp_min = -40
    temp_range = 165

    def __init__(self):
        super(Temperature, self).__init__()

        if I2C:
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

        val = self.bus.read_i2c_block_data(self.address, 0, 4)

        status = val[0] >> 6 # 2 bits for status
        H_dat = ((val[0] & 0x3f) << 8 )+ val[1] # 14 bits for humidity
        T_dat = (val[2] << 6) + (val[3] >> 2) # 14 bits for temperature

        humidity = (float(H_dat) / float(self.sensor_max)) * 100
        celsius = ((float(T_dat) / float(self.sensor_max)) * self.temp_range) + self.temp_min

        return (humidity, celsius, status)

class PluginError(Exception):
    pass

Plugin = Temperature
