import time

WIRING_PI = True
try:
	import wiringpi
except ImportError:
	WIRING_PI = False

button_pin = {
	0: 17
}

switch_pin = {
	0: 23
}

def push_button(button):
	if not WIRING_PI:
		return False

	pin = button_pin[button]

	io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
	io.pinMode(pin, io.OUTPUT)
	io.digitalWrite(pin, io.HIGH)

	time.sleep(1)
	io.digitalWrite(pin, io.LOW)

	return True

def read_switch(switch):
	if not WIRING_PI:
		return False

	pin = switch_pin[switch]

	io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)

	return io.digitalRead(pin) is io.HIGH

def flip_switch(switch):
	if not WIRING_PI:
		return False

	pin = switch_pin[switch]

	io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_SYS)
	io.pinMode(pin, io.OUTPUT)

	if read_switch(switch):
		io.digitalWrite(pin, io.LOW)
	else:
		io.digitalWrite(pin, io.HIGH)

	return True
