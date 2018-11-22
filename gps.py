import serial
import pynmea2

response = ""
with serial.Serial('/dev/ttyS1', baudrate=9600, timeout=1) as ser:
    while(response != "finished"):
        print(line)
        line = ser.readline().decode('ascii', errors='replace')
        msg = pynmea2.parse(line)
        if msg.sentence_type == 'GGA' and msg.fields.__contains__(msg.status == 'A'):
            print(msg.longitude)
            print(msg.latitude)
