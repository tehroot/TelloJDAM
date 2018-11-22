import serial
import pynmea2

response = ""
with serial.Serial('/dev/ttyS1', baudrate=9600, timeout=1) as ser:
    while(response != "finished"):
        line = ser.readline().decode('ascii', errors='replace')
        print(line)
