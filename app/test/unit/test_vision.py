from nose.tools import *
from flexmock import flexmock
from vision import Vision

import numpy

def test_one_car_closed_day():
	image_bytes = load_bytes('test/unit/one_car_closed_day.jpg')

	flexmock(Vision)
	Vision.should_receive('load_multipart_stream').and_return(image_bytes).once()
	Vision.should_receive('is_point_close_enough').and_return(True).once()
	is_closed, location = Vision('localhost', 8081).look_if_closed('test/unit/template.jpg')

	assert is_closed

def test_one_car_closed_nightlight():
	image_bytes = load_bytes('test/unit/one_car_closed_nightlight.jpg')

	flexmock(Vision)
	Vision.should_receive('load_multipart_stream').and_return(image_bytes).once()
	Vision.should_receive('is_point_close_enough').and_return(True).once()
	is_closed, location = Vision('localhost', 8081).look_if_closed('test/unit/template.jpg')

	assert is_closed

def test_two_cars_closed_nightlight():
	image_bytes = load_bytes('test/unit/two_cars_closed_nightlight.jpg')

	flexmock(Vision)
	Vision.should_receive('load_multipart_stream').and_return(image_bytes).once()
	Vision.should_receive('is_point_close_enough').and_return(True).once()
	is_closed, location = Vision('localhost', 8081).look_if_closed('test/unit/template.jpg')

	assert is_closed

def test_one_car_open_day():
	image_bytes = load_bytes('test/unit/one_car_open_day.jpg')

	flexmock(Vision)
	Vision.should_receive('load_multipart_stream').and_return(image_bytes).once()
	Vision.should_receive('is_point_close_enough').and_return(False).once()
	is_closed, location = Vision('localhost', 8081).look_if_closed('test/unit/template.jpg')

	assert not is_closed

def test_point_is_close_enough():
	assert Vision('localhost', 8081).is_point_close_enough((150, 2), (147, 0), 5)

def test_point_is_not_close_enough():
	assert not Vision('localhost', 8081).is_point_close_enough((150, 2), (20, 0), 5)

def load_bytes(path):
	with open(path, 'r') as image_file:
		image = image_file.read()

	return numpy.asarray(bytearray(image), dtype=numpy.uint8)