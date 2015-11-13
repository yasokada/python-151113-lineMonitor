from dummySerial import CDummySerial

serial = CDummySerial()

con1 = serial.Serial('/dev/ttyUSB1', 9600, 0.1)
res = con1.read()
con1.write("test")
