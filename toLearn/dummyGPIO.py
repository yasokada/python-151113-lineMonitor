'''
v0.1 2015/11/26
  - add setmode()
  - add setup()
'''

class CDummyGPIO:
	def __init__(self):
		self.BOARD = 0;
		self.OUT = 1;
		# do nothing
		return

	def setmode(self, board):
		# do nothing
		return

	def setup(self, pinnum, inout):
		# do nothing
		return

	def output(self, pinnum, onoff):
		# do nothing
		return

# Usage

'''
from dummyGPIO import CDummyGPIO
GPIO = CDummyGPIO()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)
'''
