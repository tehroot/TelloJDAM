import serial

response = ""
while(response != "Received"):
    ser = serial.Serial(port='/dev/ttyS1', baudrate=115200, timeout=2)

    response = ser.read(8)
    ser.cancel_read()
    print(repr(response))
