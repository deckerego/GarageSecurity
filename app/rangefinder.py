import serial
from config import configuration

serialPort = serial.Serial(configuration.get('rangefinder_tty'), 9600, timeout=2, bytesize=8, parity='N', stopbits=1)

def get_range():
    if serialPort.isOpen()== False:
        serialPort.open()
    else:
        pass
    response = serialPort.read(5)
    return int(response[1:])