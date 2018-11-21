import serial

response = ""
while(response != "Received"):
    ser = serial.Serial(port='/dev/ttyS1', baudrate=9600, timeout=100)
    response = ser.read(45)
    ser.cancel_read()
    print(response)
