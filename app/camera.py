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
        #self.stream = io.BytesIO()
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
        self.camera.close()
        
    def start(self):
        logger.info("Opening Camera Connection")
        thread.start_new_thread(self.read_camera, ())

    def get_stream(self):
        with self.stream.lock:
            for frame in self.stream.frames:
                if frame.header:
                    self.stream.seek(frame.position)
                    break
            output = io.BytesIO()
            output.write(self.stream.read())
            output.seek(0)
            print "Getting stream buffer"
            return output

    def read_camera(self):
        #buffer = io.BytesIO()

        print "Enter camera loop"
        self.camera = picamera.PiCamera()

        try:
            print "Getting camera snapshot"
            #self.camera.resolution = (1280, 720)
            self.camera.resolution = (640, 480)
            self.camera.start_preview()
            time.sleep(2)

            self.stream = picamera.PiCameraCircularIO(self.camera, seconds=10)
            self.camera.start_recording(self.stream, format='mjpeg')
            print "Recording camera snapshot"

            while True:
                self.camera.wait_recording(5)

        except:
            print "Unexpected camera error: %s", sys.exc_info()[0]
            logger.error("Unexpected camera error: %s", sys.exc_info()[0])

        finally:
            print "Closing camera"
            self.camera.stop_recording()
            self.camera.close()


class PluginError(Exception):
    pass

Plugin = Camera
