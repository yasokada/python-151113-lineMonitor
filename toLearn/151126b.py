import time

#--- selection of import based on the package ---
''' 1. with RPi.GPIO'''
#import RPi.GPIO as GPIO
''' 2. without RPi.GPIO'''
from dummyGPIO import CDummyGPIO
GPIO = CDummyGPIO()
#-----------------

GPIO.setmode(GPIO.BOARD)

#-------------------
#[User Configuration]
# Pin# of RPi2 (Change according to the cable connections)
pinnum=[3, 5, 7, 11, 13, 15, 19, 21]
#-------------------
#[Do no change followings]
# onoff bit (7segment led > a..g)
onoff=[ 
[True,  True, True, True,  True,      True,  True,  False ], # disp 0
[False, True, True, False, False,     False, False, False ], # disp 1
[True,  True, False, True,  True,      False,  True, False ], # disp 2
[True,  True, True,  True, False,      False, True, False], # disp 3
[False, True, True, False, False,      False, True,  False ], # disp 4
[True, False, True, True, False,       True,  True, False], # disp 5
[True, False, True, True,  True,       True, True, False], # disp 6
[True, True, True, False, False,       True, False, False], # disp 7
[True, True, True,  True,  True,       True, True, False], # disp 8
[True, True, True,  True,  False,       True, True, False], # disp 9
[False, False, False, False, False,     False, False, True], # disp .
]
# TODO: 0z > add out of range display
# TODO: 0z > add all off function
#-------------------

def info7seg_init():
	print "init"
	for idx in range(0, len(pinnum)): 
		GPIO.setup(pinnum[idx], GPIO.OUT) # a..h

def info7seg_on(number):
	print "on"
	for idx in range(0, len(pinnum)): # a..h
		GPIO.output(pinnum[idx], onoff[number][idx])

info7seg_init()
info7seg_on(2)
time.sleep(1)
info7seg_on(7)
time.sleep(1)
info7seg_on(1)
time.sleep(1)
