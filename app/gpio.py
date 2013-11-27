import time

WIRING_PI = True
try:
	import wiringpi
except ImportError:
	WIRING_PI = False

button_pin = {
	0: 17
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
