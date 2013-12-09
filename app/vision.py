import cv2
import socket
import sys 
import numpy

CV_LOAD_IMAGE_UNCHANGED = -1
CV_LOAD_IMAGE_GRAYSCALE = 0

class Vision:

	def __init__(self, host, port):
		self.host = host
		self.port = port

	def look_if_closed(self, template_path, template_location, template_margin=5):
		base_bytes = self.load_multipart_stream()
		base = cv2.imdecode(base_bytes, CV_LOAD_IMAGE_GRAYSCALE)
		template = cv2.imread(template_path, CV_LOAD_IMAGE_GRAYSCALE)

		res = cv2.matchTemplate(base, template, cv2.TM_CCOEFF_NORMED)
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

		is_closed = self.is_point_close_enough(max_loc, template_location, template_margin)
		return is_closed, max_loc

	def load_multipart_stream(self):
		http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		http_socket.connect((self.host, self.port))
		 
		file_handle = http_socket.makefile()
		http_line = file_handle.readline().strip()

		while http_line != '': 
		    header_entry = http_line.split(':')

		    if 'content-type' in header_entry[0].lower():
		        content_type = header_entry[1].strip()
		        boundary = content_type.split(';')[1].split('=')[1]

		    http_line = file_handle.readline().strip()
		 
		if not boundary:
		    raise Exception("No content type provided in HTTP response")
		 
		while http_line != boundary:
		    http_line = file_handle.readline().strip()
		
		while http_line != '': 
		    header_entry = http_line.split(':')
		    if 'content-length' in header_entry[0].lower():
		        chunk_length = int(header_entry[1].strip())

		    http_line = file_handle.readline().strip()
		 
		image = file_handle.read(chunk_length)
		image_bytes = numpy.asarray(bytearray(image), dtype=numpy.uint8)
		 
		http_socket.close()

		return image_bytes

	def is_point_close_enough(self, point, expected, margin):
		x_margin = (point[0] <= expected[0] + margin) and (point[0] >= expected[0] - margin)
		y_margin = (point[1] <= expected[1] + margin) and (point[1] >= expected[1] - margin)
		return x_margin and y_margin