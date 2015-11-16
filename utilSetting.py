class CSetting:
	def __init__(self):
		self.monip = "192.168.10.8"
		self.monport = 9000
		self.comdelay = 0 # [msec]
		self.cmdport = 7000
		self.combaud = 9600
		self.baudchange = False

	def getCombaud(self):
		return self.combaud

	def setCombaud(self,combaud_):
		self.combaud = combaud_
		self.baudchange = True
		return

	def getBaudChange(self):
		return self.baudchange

	def getMonip(self):
		return self.monip

	def setMonip(self,monip_):
		self.monip = monip_
		return

	def getMonport(self):
		return self.monport

	def setMonport(self,monport_):
		self.monport = monport_
		return

	def getComdelay(self):
		return self.comdelay

	def setComdelay(self, comdelay_):
		self.comdelay = comdelay_
		return

	def getCmdPort(self):
		return self.cmdport

# TODO: 0m> get/set current ip address of RPi2
