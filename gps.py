import serial
import pynmea2

response = ""
while(response != "Received"):
    ser = serial.Serial(port='/dev/ttyS1', baudrate=9600, timeout=100)
    response = ser.read(41)
    ser.cancel_read()
    msg = pynmea2.parse(response)
    print(msg)

