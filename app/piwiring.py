WIRING_PI = True
try:
    import wiringpi
except ImportError:
    WIRING_PI = False
    logger.error("Cannot initialize GPIO - Library Not Installed?")

import inspect
import logging
import time

logger = logging.getLogger('garagesec')
logger.setLevel(20)

class GPIO(object):
    name = 'gpio'
    keyword = 'gpio'
    initialized = False
    button_pin = {
        0: 17
    }
    switch_pin = {
        0: 23
    }

    def __init__(self):
        super(GPIO, self).__init__()

    def __del__(self):
        self.close()

    # This is invoked when installed as a Bottle plugin
    def setup(self, app):
        self.routes = app

        for other in app.plugins:
            if not isinstance(other, GPIO):
                continue
            if other.keyword == self.keyword:
                raise PluginError("Found another instance of GPIO running!")

    # This is invoked within Bottle as part of each route when installed
    def apply(self, callback, route):
        # Lazy initialization
        if not self.initialized:
            self.initialized = True
            self.init()

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
        logger.info("Closing GPIO Connection")

    # For some reason wiringPi can't be initialized on import or setup or construction... that's too soon.
    def init(self):
        wiringpi.wiringPiSetupSys()

    def push_button(self, button):
        if not WIRING_PI:
            logger.warn("Pushed button but no GPIO initialized")
            return False

        pin = self.button_pin[button]

        wiringpi.pinMode(pin, 1)
        wiringpi.digitalWrite(pin, 1)

        time.sleep(1)
        wiringpi.digitalWrite(pin, 0)

        return True

    def read_switch(self, switch):
        if not WIRING_PI:
            return False

        pin = self.switch_pin[switch]

        return wiringpi.digitalRead(pin) > 0

    def flip_switch(self, switch):
        if not WIRING_PI:
            logger.warn("Flipped switch but no GPIO initialized")
            return False

        pin = self.switch_pin[switch]

        wiringpi.pinMode(pin, 1)

        if self.read_switch(switch):
            wiringpi.digitalWrite(pin, 0)
        else:
            wiringpi.digitalWrite(pin, 1)

        return True
