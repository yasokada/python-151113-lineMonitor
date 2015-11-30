import os.path

'''
v0.2  2015/11/30
	- update add() to handle auto save feature
v0.1  2015/11/30
	- add save()
	- add add()
	- add __init__()
'''

class CUtilLogger:
	def __init__(self, saveto):
		self.idx = 0
		self.maxnum = 5
		self.strs = [ "", "", "", "", "", ""]
		self.saveto = saveto
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
		with open(self.saveto, "a") as logfd:
			for idx in range(0, self.idx):
				text = self.strs[idx] + "\r\n"
				logfd.write(text)	

#Usage 
logger = CUtilLogger("151130.log")
for loop in range(0, 31):
	logger.add("test")
logger.save() # to save the rest
logger = None



