import time

for loop in range(0,3):
	msec = int(round(time.time() * 1000)) % 1000
	print msec
	time.sleep(0.1)