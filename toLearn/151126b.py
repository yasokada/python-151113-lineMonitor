import time

#--- selection of import based on the package ---
''' 1. with RPi.GPIO'''
#import RPi.GPIO as GPIO
''' 2. without RPi.GPIO'''
from dummyGPIO import CDummyGPIO
GPIO = CDummyGPIO()
#-----------------

# TODO: 0m > dummyGPIO

GPIO.setmode(GPIO.BOARD)

#-------------------
# Pin# of RPi2 (changes according to connection)
pinnum=[3, 5, 7, 11, 13, 15, 19, 21]
#-------------------
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
#-------------------
codes=[ 3, 1, 4, 1]

# 1. setup
for idx in range(0, len(pinnum)):
	GPIO.setup(pinnum[idx], GPIO.OUT)

# 2. 7seg LED on
for idx in range(0, len(pinnum)): # a..g
	GPIO.setup(pinnum[idx], onoff[3][idx])
time.sleep(5.0)

print "-------"

'''
for digit in range(0, 4): # TODO: 1> size of
	code = codes[digit]
	print code
	for idx in range(0, len(pinnum)): # a..g
		print pinnum[idx], onoff[code][idx]
	time.sleep(1.0)
'''