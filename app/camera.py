import picamera
import io
import time
import thread
import threading
import inspect
import logging
import math
import operator
import urllib2
from PIL import Image
from config import configuration

logger = logging.getLogger('garagesec')

class Camera(object):
    name = 'camera_rpi'
    keyword = 'camera'

    def __init__(self):
        super(Camera, self).__init__()
        self.image_bin = b""
        self.stream_lock = threading.RLock()
        self.difference = 0
        self.difference_threshold = 10000
        self.start()

    def __del__(self):
        self.close()

    # This is invoked when installed as a Bottle plugin
    def setup(self, app):
        self.routes = app

        for other in app.plugins:
            if not isinstance(other, Camera):
                continue
            if other.keyword == self.keyword:
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

    def get_difference(self):
        return self.difference

    def read_camera(self):
        buffer = io.BytesIO()

        with picamera.PiCamera() as camera:
            camera.resolution = (1280, 720)
            camera.vflip = True
            camera.hflip = True
            camera.exposure_mode = 'night'
            camera.start_preview()
            time.sleep(2)

            for nothing in camera.capture_continuous(buffer, format='jpeg', use_video_port=True):
                buffer.seek(0)

                previous_image_stream = self.get_still()
                with self.stream_lock:
                    self.image_bin = buffer.getvalue()

                self.difference = compare(previous_image_stream, self.get_still())
                if self.difference >= self.difference_threshold:
                    request = urllib2.Request('http://localhost/camera/motion', '')
                    request.add_header("Authorization", "Basic %s" % configuration.get('api_basic_auth'))
                    urllib2.urlopen(request)

                buffer.seek(0)
                buffer.truncate()

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