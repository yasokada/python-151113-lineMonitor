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

numsegs=8 # a..g

for digit in range(0, 4): # TODO: 1> size of
	code = codes[digit]
	print code
	for idx in range(0, numsegs):
		print pinnum[idx], onoff[code][idx]
