from utilUdpCmd import recvCommand, procCommand, getSetting
from utilSetting import CSetting
from utilComRelay import comrelay
import socket

#--- selection of import based on the package ---
''' with python3-serial'''
#import serial
''' without python3-serial'''
from dummySerial import CDummySerial
serial = CDummySerial()
#-----------------

# HACKME: something does not sit right concerning "setting" passing (g_setting)

g_setting = CSetting() # for having g_setting as global

def main():
	# command udp setting
	cmdip = ""
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

	while 1:
		g_setting = getSetting() # HACKME: 

		rcvd1,isNL = comrelay(rcvd1, con1, con2)
		if isNL == True:
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
