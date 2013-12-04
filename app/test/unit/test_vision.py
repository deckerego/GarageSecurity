from nose.tools import *
from flexmock import flexmock

import vision

def test_one_car_closed_day():
	assert vision.look_if_closed('test/unit/one_car_closed_day.jpg', 'test/unit/template.jpg')

def test_one_car_closed_nightlight():
	assert vision.look_if_closed('test/unit/one_car_closed_nightlight.jpg', 'test/unit/template.jpg')

def test_two_cars_closed_nightlight():
	assert vision.look_if_closed('test/unit/two_cars_closed_nightlight.jpg', 'test/unit/template.jpg')

def test_one_car_open_day():
	assert not vision.look_if_closed('test/unit/one_car_open_day.jpg', 'test/unit/template.jpg')
