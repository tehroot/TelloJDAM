import pynmea2

msg = '$GPGGA,024050.000,3957.7748,N,07511.8180,W,1,4,2.30,81.6,M,-33.9,M,,*54'
line = pynmea2.parse(msg)
print(line.latitude)
print(line.longitude)
