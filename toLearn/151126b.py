#-------------------
# Pin# of RPi2 (changes according to connection)
pinnum=[3, 5, 7, 11, 13, 15, 19, 21]
#-------------------
# onoff bit (7segment led > a..g)
onoff=[ 
[True,  True, True, True,  True,      True,  True,  False ], # disp 0
[False, True, True, False, False,     False, False, False ], # disp 1
# TODO: 1> disp 2..9
[False, False, False, False, False,   False, False, False], # dummy 2
[False, False, False, False, False,   False, False, False], # dummy 3
[False, False, False, False, False,   False, False, False], # dummy 4
[False, False, False, False, False,   False, False, False], # dummy 5
[False, False, False, False, False,   False, False, False], # dummy 6
[False, False, False, False, False,   False, False, False], # dummy 7
[False, False, False, False, False,   False, False, False], # dummy 8
[False, False, False, False, False,   False, False, False], # dummy 9
]
#-------------------
codes=[ 3, 1, 4, 1]

numsegs=8 # a..g

for digit in range(0, 4): # TODO: 1> size of
	code = codes[digit]
	print code
	for idx in range(0, numsegs):
		print pinnum[idx], onoff[digit - 1][idx]
