import serial
import pynmea2

response = ""
while(response != "Received"):
    ser = serial.Serial(port='/dev/ttyS1', baudrate=9600, timeout=100)
    response = ser.readline().decode('ascii', errors='replace')
    streamreader = pynmea2.NMEAStreamReader()
    while 1:
        data = input().read()
        for msg in streamreader.next(data):
            print(msg)
    ser.cancel_read()

