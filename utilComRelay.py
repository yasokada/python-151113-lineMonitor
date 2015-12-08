
#--- selection of import based on the package ---
''' 1. with python3-serial'''
import serial
''' 2. without python3-serial'''
#from dummySerial import CDummySerial
#serial = CDummySerial()
#-----------------

'''
v0.2 2015/12/09
  - comrelay() takes "\r" also as new line

v0.1 2015/11/12
  - add comrelay()
  - add comReopen() 
'''

import time

def comrelay(rcvd, srccom, dstcom):
    str1 = srccom.read()
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

