import time

WIRING_PI = True
try:
	import wiringpi
	wiringpi.wiringPiSetupSys()
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

	wiringpi.pinMode(pin, 1)
	wiringpi.digitalWrite(pin, 1)

	time.sleep(1)
	wiringpi.digitalWrite(pin, 0)

	return True

def read_switch(switch):
	if not WIRING_PI:
		return False

	pin = switch_pin[switch]

	return wiringpi.digitalRead(pin) > 0

def flip_switch(switch):
	if not WIRING_PI:
		return False

	pin = switch_pin[switch]

	wiringpi.pinMode(pin, 1)

	if read_switch(switch):
		wiringpi.digitalWrite(pin, 0)
	else:
		wiringpi.digitalWrite(pin, 1)

	return True
