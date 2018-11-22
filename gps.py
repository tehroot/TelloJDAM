import serial
import pynmea2

response = ""
with serial.Serial('/dev/ttyS1', baudrate=9600, timeout=1) as ser:
    while(response != "finished"):
        line = ser.readline().decode('ascii', errors='replace')
        print(line)
        msg = pynmea2.parse(line)
        if msg.sentence_type == 'GGA':
            #print(msg.longitude)
            #print(msg.latitude)
        if msg.sentence_type == 'RMC' and msg.fields.__contains__(msg.status == 'A'):
            print(msg.latitude)
            print(msg.longitude)

