
#--- selection of import based on the package ---
''' 1. with python3-serial'''
import serial
''' 2. without python3-serial'''
#from dummySerial import CDummySerial
#serial = CDummySerial()
#-----------------

'''
v0.3 2016 Feb. 16
  - handle control character without <CR>,<LF> such as <ACK>, <NAK>
v0.2 2015/12/09
  - comrelay() takes "\r" also as new line
v0.1 2015/11/12
  - add comrelay()
  - add comReopen() 
'''

## TODO: 0m > send <ACK>,etc as "<ACK>" to Udp monitor terminal

import time

def isControlCharOtherThanCRLF(code):
    if ord(code) == 13 or ord(code) == 10:
        return False
    return ord(code) < 32 

def comrelay(rcvd, srccom, dstcom):
    str1 = srccom.read()
    if len(str1) > 0 and isControlCharOtherThanCRLF(str1):
        print "rcvd:control char:" + str(ord(str1))
        dstcom.write(rcvd)
        return ".", True # new line = true
    if (len(str1) > 0):
        rcvd = rcvd + str1
    if "\n" in rcvd or "\r" in rcvd:
        print "rcvd=", rcvd
        dstcom.write(rcvd)
        return rcvd, True # new line = true

    return rcvd, False # new line = false

def comReopen(con1, con2, combaud):
	con1.close()
	con2.close()
	time.sleep(0.1) # TODO: 1> not sure necessary or not
	con1 = serial.Serial('/dev/ttyUSB1', combaud, timeout=0.1)
	con2 = serial.Serial('/dev/ttyUSB0', combaud, timeout=0.1)
	return

