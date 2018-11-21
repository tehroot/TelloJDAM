import serial
import pynmea2

response = ""
with serial.Serial('/dev/ttyS1', baudrate=9600, timeout=1) as ser:
    while(respone != "finished"):
        line = ser.readline().decode('ascii', errors='replace')
        msg = pynmea2.parse(line.strip())
        print(msg)
        print(msg.lat)
