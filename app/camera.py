import picamera
import io
import numpy
from PIL import Image

def get_still():
	with picamera.PiCamera() as camera:
		camera.resolution = (1440, 1080)
		camera.vflip = True
		camera.hflip = True
		camera.exposure_mode = 'night'
		stream = io.BytesIO()
		camera.capture(stream, format='jpeg', use_video_port=True)
		stream.flush()
		stream.seek(0)
		return stream
