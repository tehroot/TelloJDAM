import serial
import pynmea2
import sys


def connect_serial():
    try:
        while True:
            with serial.Serial('/dev/ttyS1', baudrate=9600, timeout=1) as ser:
                line = ser.readline().decode('ascii', errors='replace')
                return line
    except Exception as e:
        sys.stderr.write("Error connecting to UART" % type(e).__name__, e)
    except KeyboardInterrupt as e:
        sys.stderr.write("Keyboard Interrupt")


def get_gps(line):
    try:
        while line:
            msg = pynmea2.parse(line)
            if msg.sentence_type == 'GGA' and msg.gps_qual == 1:
                print(msg.longitude)
                print(msg.latitude)
                line = ''
            elif msg.sentence_type == 'GGA' and msg.gps_qual == 0:
                print("...awaiting gps fix")
    except KeyboardInterrupt:
        sys.stderr.write("Keyboard Interrupt")


def main():
    try:
        while True:
            message = connect_serial()
            get_gps(message)
    except KeyboardInterrupt:
        sys.stderr.write('Ctrl-C KeyboardInterrupt')
