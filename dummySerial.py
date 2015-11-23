
'''
v0.2 2015/11/23
  - add close()
v0.1 2015/11/13
  - add dummySerial.py
'''

class CDummySerial:
	def __init__(self):
		# do nothing
		return

	def read(self):
		# do nothing
#		print "read:" # TODO: 0 > remove
		return ""

	def write(self,txstr):
		# do nothing
#		print "write:", txstr # TODO: 0 > remove
		return ""

	def close(self):
		# do nothing
		return ""

	@staticmethod
	def Serial(name, baud, timeout):
		work = CDummySerial()
		return work

# Usage

'''
from dummySerial import CDummySerial

serial = CDummySerial()

con1 = serial.Serial('/dev/ttyUSB1', 9600, 0.1)
res = con1.read()
con1.write("test")
'''


