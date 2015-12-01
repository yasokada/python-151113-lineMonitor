import os.path
import datetime

'''
v0.5  2015/12/01
	- remove CRLF at the end of the line
	- save to Log/
	- use [0] * 10 to declare a List
	- add time stamp to the save strings
v0.4  2015/11/30
	- comment out test run
	- add from sentence to import CUtilLogger
v0.3  2015/11/30
	- change array declaration to those using range()
	- __init__() does not take saveto arg 
	- automatically get file name based on the date
v0.2  2015/11/30
	- update add() to handle auto save feature
v0.1  2015/11/30
	- add save()
	- add add()
	- add __init__()
'''

class CUtilLogger:
	def __init__(self):
		self.idx = 0
		self.bufferNum = 5
		self.strs = [0] * 10
		return

	def clear(self):
		for idx in range(0, self.idx):
			self.strs[idx] = ""
		self.idx = 0

	def add(self,str):
		today = datetime.datetime.today()
		yymmddhhnnss = today.strftime("%Y/%m/%d,%H:%M:%S")
		text = yymmddhhnnss + "," + str
		self.strs[self.idx] = text
		self.idx = self.idx + 1
#		print self.idx
		if self.idx >= self.bufferNum:
			self.save()
			self.clear()

	def makeFolder(self):
		if os.path.isdir("Log") == False:
			os.mkdir("Log")

	def save(self):
		self.makeFolder()
		today = datetime.datetime.today()
		yymmdd = today.strftime("%y%m%d")
		filename = "Log/" + yymmdd + ".log"
		with open(filename, "a") as logfd:
			for idx in range(0, self.idx):
				text = self.strs[idx]
				logfd.write(text)	

# Usage 

'''
import time
from utilLogger import CUtilLogger
logger = CUtilLogger()

for loop in range(0, 31):
	logger.add("test")
	time.sleep(0.3)
logger.save() # to save the rest
logger = None
'''

# TODO: 0m > save to folder (Log/)
