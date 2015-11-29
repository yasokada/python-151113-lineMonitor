import os.path
import time

if os.path.isdir("Log") == False:
	os.mkdir("Log")

for loop in range(0,3):
	with open("Log/151130.txt", "a") as logfd:
		logfd.write("test\r\n")
	print loop
	time.sleep(5)