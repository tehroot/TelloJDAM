import serial
import pynmea2

response = ""
with serial.Serial('/dev/ttyS1', baudrate=9600, timeout=1) as ser:
    while(response != "finished"):
        msg = pynmea2.parse(ser.readline().decode('ascii', errors='replace'), check=True)
        print(msg)
