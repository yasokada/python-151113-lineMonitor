
#--- selection of import based on the package ---
''' with python3-serial'''
#import serial
''' without python3-serial'''
from dummySerial import CDummySerial
serial = CDummySerial()
#-----------------

def comrelay(rcvd, srccom, dstcom):
    str1 = srccom.read()
    if (len(str1) > 0):
        rcvd = rcvd + str1
    if "\n" in rcvd:
        print "rcvd=", rcvd
        dstcom.write(rcvd)
        return rcvd, True # new line = true

    return rcvd, False # new line = false

