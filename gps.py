import serial
import pynmea2

response = ""
with serial.Serial('/dev/ttyS1', baudrate=9600, timeout=1) as ser:
    while(response != "finished"):
        line = ser.readline().decode('ascii', errors='replace')
        print(line)
        msg = pynmea2.parse(line)
        if msg.sentence_type == 'GGA' and msg.gps_qual == 1:
            print(msg.longitude)
            print(msg.latitude)
