import serial

response = ""
while(response != "Received"):
    ser = serial.Serial(port='/dev/ttyS1', baudrate=9600, timeout=5)

    response = ser.read(8)
    ser.cancel_read()
    print(repr(response))
