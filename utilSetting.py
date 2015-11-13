class CSetting:
	def __init__(self):
		self.monip = "192.168.10.8"
		self.monport = 9000

	def getMonip(self):
		return self.monip

	def setMonip(self,monip_):
		self.monip = monip_
		return self.monip
	