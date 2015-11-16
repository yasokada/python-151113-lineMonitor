from utilUdpCmd import recvCommand, procCommand, getSetting
from utilSetting import CSetting
from utilComRelay import comrelay
import socket

#--- selection of import based on the package ---
''' 1. with python3-serial'''
#import serial
''' 2. without python3-serial'''
from dummySerial import CDummySerial
serial = CDummySerial()
#-----------------

# HACKME: something does not sit right concerning "setting" passing (g_setting)

g_setting = CSetting() # for having g_setting as global

def main():
	# command udp setting
	cmdip = "" # INADDR_ANY
	g_setting = getSetting() # HACKME: 
	cmdport = g_setting.getCmdPort()
	cmdsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	cmdsock.bind((cmdip, cmdport))
	cmdsock.setblocking(0)
	# monitor udp setting (no binding)
	monip = g_setting.getMonip()
	monport = g_setting.getMonport()
	monsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	# COM setting
	con1=serial.Serial('/dev/ttyUSB1', 9600, timeout=0.1)
	con2=serial.Serial('/dev/ttyUSB0', 9600, timeout=0.1)

	print "cmdport=", cmdport

	rcvd1 = ""
	rcvd2 = ""
	rcvcmd = ""	

# TODO: 0z > add COM delay feature

	while 1:
		#HACKME: ---- calling getSetting(), then, g_setting.getXXX() is not a good style
		g_setting = getSetting()
		monip = g_setting.getMonip()
		monport = g_setting.getMonport()

		rcvd1,isNL = comrelay(rcvd1, con1, con2)
		if isNL == True: # new line
			monsock.sendto("1:" + rcvd1, (monip, monport))
			rcvd1 = ""
		
		rcvd2,isNL = comrelay(rcvd2, con2, con1)
		if isNL == True:
			monsock.sendto("2:" + rcvd2, (monip, monport))
			rcvd2 = ""

		rcvcmd,rcvd = recvCommand(cmdsock, rcvcmd)
		if rcvd == True and "\n" in rcvcmd:
			procCommand(rcvcmd)
			rcvcmd = ""

if __name__ == '__main__':
	main()
