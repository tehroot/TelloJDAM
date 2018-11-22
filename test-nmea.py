import pynmea2

line = '$GPGGA,024050.000,3957.7748,N,07511.8180,W,1,4,2.30,81.6,M,-33.9,M,,*54'
msg = pynmea2.parse(line)
print(msg.sentence_type)
if msg.sentence_type == 'GGA':
    print(msg.longitude)
    print(msg.latitude)
