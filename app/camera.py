import picamera
import io
import time
import thread
import inspect
import logging
from config import configuration

logger = logging.getLogger('garagesec')

class Camera(object):
    name = 'camera_rpi'
    keyword = 'camera'

    def __init__(self):
        super(Camera, self).__init__()
        self.stream = io.BytesIO()
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

    def get_stream(self):
        self.stream.seek(0)
        print "Getting stream buffer"
        return self.stream

    def read_camera(self):
        buffer = io.BytesIO()

        while True:
            print "Enter camera loop"
            try:
                with picamera.PiCamera() as camera:
                    print "Getting camera snapshot"
                    #camera.resolution = (1280, 720)
                    camera.resolution = (640, 480)
                    camera.start_preview()
                    time.sleep(2)
                    camera.start_recording(buffer, format='mjpeg')
                    print "Recording camera snapshot"
                    camera.wait_recording(5)
                    camera.stop_recording()
            except:
                print "Unexpected camera error: %s", sys.exc_info()[0]
                logger.error("Unexpected camera error: %s", sys.exc_info()[0])

            self.stream = buffer


class PluginError(Exception):
    pass

Plugin = Camera
