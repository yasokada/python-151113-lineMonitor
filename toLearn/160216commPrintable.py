#!/usr/bin/env python

import serial
import time

def isControlCharOtherThanCRLF(code):
    if ord(code) == 13 or ord(code) == 10:
        return False
    return ord(code) < 32

def main():
    con=serial.Serial('/dev/ttyUSB0', 9600, timeout=10)
    rcvd=''
    while 1:
        code = con.read()
        if len(code) > 0:
            if isControlCharOtherThanCRLF(code):
                print "control char:" + str(ord(code))
            else:
                rcvd = rcvd + code
        if "\n" in rcvd or "\r" in rcvd:
            print rcvd,
            rcvd = ''
        
main()
