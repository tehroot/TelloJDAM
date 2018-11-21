import serial

with serial.Serial('/dev/ttyS1', baudrate=9600, timeout=1) as ser:
    for i in range(10):
        line = ser.readline().decode('ascii', errors='replace')
        print(line.strip)
