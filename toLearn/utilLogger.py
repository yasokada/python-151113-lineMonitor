import os.path
import datetime

'''
v0.3  2015/11/30
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
		self.maxnum = 5
		self.strs = [ "", "", "", "", "", ""]
		return

	def clear(self):
		for idx in range(0, self.idx):
			self.strs[idx] = ""
		self.idx = 0

	def add(self,str):
		self.strs[self.idx] = str
		self.idx = self.idx + 1
		print self.idx
		if self.idx >= self.maxnum:
			self.save()
			self.clear()

	def save(self):
		today = datetime.date.today()
		yymmdd = today.strftime("%y%m%d")
		filename = yymmdd + ".log"
		with open(filename, "a") as logfd:
			for idx in range(0, self.idx):
				text = self.strs[idx] + "\r\n"
				logfd.write(text)	

#Usage 
logger = CUtilLogger()
for loop in range(0, 31):
	logger.add("test")
logger.save() # to save the rest
logger = None



