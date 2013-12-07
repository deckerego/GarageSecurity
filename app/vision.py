import cv2
import socket
import sys 
import numpy

CV_LOAD_IMAGE_UNCHANGED = -1

def look_if_closed(image_path='http://localhost:8081', template_path='closed_template.jpg'):
	base = cv2.imdecode(load_multipart_stream('localhost', 8081), CV_LOAD_IMAGE_UNCHANGED)
	template = cv2.imread(template_path, CV_LOAD_IMAGE_UNCHANGED)

	res = cv2.matchTemplate(base, template, cv2.TM_CCOEFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

	return max_loc[0] > 5, max_loc

def load_multipart_stream(host, port):
	http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	http_socket.connect((host, port))
	 
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