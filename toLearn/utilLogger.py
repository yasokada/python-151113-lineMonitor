import os.path

'''
v0.1  2015/11/30
	- add save()
	- add add()
	- add __init__()
'''

class CUtilLogger:
	def __init__(self, saveto):
		self.idx = 0
		self.strs = [ "", "", "", "", "", ""]
		self.saveto = saveto
		return

	def add(self,str):
		self.strs[self.idx] = str
		self.idx = self.idx + 1
		print self.idx
	
	def save(self):
		with open(self.saveto, "a") as logfd:
			for idx in range(0, self.idx):
				text = self.strs[idx] + "\r\n"
				logfd.write(text)	

#Usage 
logger = CUtilLogger("151130.log")
logger.add("test")
logger.add("test")
logger.add("test")
logger.save()
logger = None

# TODO: 0m > auto save if idx > 5


