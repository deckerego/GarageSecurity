import picamera
import io
import time
import thread
import threading
import inspect
import logging
import math
import operator
import jabber
import sys
from PIL import Image
from config import configuration

logger = logging.getLogger('garagesec')

class Camera(object):
    name = 'camera_rpi'
    keyword = 'camera'

    def __init__(self):
        super(Camera, self).__init__()
        self.image_bin = b""
        self.difference = 0
        self.difference_threshold = 10000
        # Give the camera 10 seconds to warm up
        self.last_alert = time.time() - configuration.get('cooldown_period') + 10
        self.jabber = None
        self.start()

    def __del__(self):
        self.close()

    # This is invoked when installed as a Bottle plugin
    def setup(self, app):
        self.routes = app

        for other in app.plugins:
            if isinstance(other, Camera) and other.keyword == self.keyword:
                raise PluginError("Found another instance of Camera running!")

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
        logger.info("Closing Camera Connection")
        
    def start(self):
        logger.info("Opening Camera Connection")
        thread.start_new_thread(self.read_camera, ())

    def get_still(self):
        return io.BytesIO(self.image_bin)

    def get_jabber(self):
        if not self.jabber:
            for other in self.routes.plugins:
                if isinstance(other, jabber.Jabber):
                    self.jabber = other
        return self.jabber

    def get_difference(self):
        return self.difference

    def get_last_event(self):
        return self.last_alert

    def read_camera(self):
        buffer = io.BytesIO()

        with picamera.PiCamera() as camera:
            camera.resolution = (1280, 720)
            camera.vflip = True
            camera.hflip = True
            camera.exposure_mode = 'night'

            for nothing in camera.capture_continuous(buffer, format='jpeg', use_video_port=True):
                try:
                    buffer.seek(0)

                    previous_image_stream = self.get_still()
                    self.image_bin = buffer.getvalue()

                    self.difference = compare(previous_image_stream, self.get_still())
                    event_time = time.time()
                    next_event = self.last_alert + configuration.get('cooldown_period')

                    if (self.difference >= self.difference_threshold) and (event_time >= next_event):
                        self.last_alert = event_time
                        self.get_jabber().send_alert()

                    buffer.seek(0)
                    buffer.truncate()
                except:
                    logger.error("Unexpected error: %s" % sys.exc_info()[0])

def compare(stream1, stream2):
    rms = -1
    try:
        image1 = Image.open(stream1)
        image2 = Image.open(stream2)
        h1 = image1.histogram()
        h2 = image2.histogram()
        rms = [(h1[i] - h2[i]) ** 2 for i in xrange(len(h1))]; rms = math.sqrt(sum(rms) / len(h1));
    except Exception as e:
        logger.warn("Could not compare images: %s" % e)
    finally:
        return rms

class PluginError(Exception):
    pass

Plugin = Camera