from utilUdpCmd import recvCommand, procCommand, getSetting
from utilSetting import CSetting
import socket

#--- selection of import based on the package ---
''' with python3-serial'''
#import serial
''' without python3-serial'''
from dummySerial import CDummySerial
serial = CDummySerial()
#-----------------

# HACKME: something does not sit right concerning "setting" passing (g_setting)

g_setting = CSetting()

def main():
	# command setting
	cmdip = ""
	g_setting = getSetting() # HACKME: 
	cmdport = g_setting.getCmdPort()
	cmdsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	cmdsock.bind((cmdip, cmdport))
	cmdsock.setblocking(0)
	# monitor setting (no binding)
	monip = g_setting.getMonip()
	monport = g_setting.getMonport()
	monsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# COM setting
	con1=serial.Serial('/dev/ttyUSB1', 9600, timeout=0.1)
	con2=serial.Serial('/dev/ttyUSB0', 9600, timeout=0.1)

	print "cmdport=", cmdport

	rcvcmd = ""

	while 1:
		g_setting = getSetting() # HACKME: 
		rcvcmd,rcvd = recvCommand(cmdsock, rcvcmd)
		if rcvd == True and "\n" in rcvcmd:
			procCommand(rcvcmd)
			rcvcmd = ""

if __name__ == '__main__':
	main()
