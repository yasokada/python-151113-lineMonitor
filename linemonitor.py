#!/usr/bin/env python
from utilUdpCmd import recvCommand, procCommand, getSetting
from utilSetting import CSetting
from utilComRelay import comrelay, comReopen
from utilLogger import CUtilLogger
import socket

#--- selection of import based on the package ---
''' 1. with python3-serial'''
import serial
''' 2. without python3-serial'''
#from dummySerial import CDummySerial
#serial = CDummySerial()
#-----------------


'''
v0.7 2015/12/02
  - change prefix string from "1:" to "rcvd1," for csv handling
  - save Log feature
v0.6 2015/11/28
  - add 1st line for auto start at /etc/rc.local
v0.5 2015/11/21
  - tweak Seiral timeout to fix slowness of the communication 
v0.4 2015/11/21
  - fix bug on monport > TypeError: an integer is required
v0.3 2015/11/16
  - can change combaud (but not using comReopen())
  - add get/set settings (combaud)
v0.2 2015/11/13
  - add dummySerial.py
v0.1 2015/11/13
  - can get/set settings (monitor ip, monitor port, com delay[msec])
'''

# HACKME: something does not sit right concerning "setting" passing (g_setting)

g_setting = CSetting() # for having g_setting as global
logger = CUtilLogger()

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
	con1=serial.Serial('/dev/ttyUSB1', 9600, timeout=0.001)
	con2=serial.Serial('/dev/ttyUSB0', 9600, timeout=0.001)

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

		if g_setting.getBaudChange() == True:
#			comReopen( con1, con2, g_setting.getCombaud() )
			con1.close()
			con2.close()
			combaud = g_setting.getCombaud()
			con1=serial.Serial('/dev/ttyUSB1', combaud, timeout=0.001)
			con2=serial.Serial('/dev/ttyUSB0', combaud, timeout=0.001)
			g_setting.setBaudChange(False)

		rcvd1,isNL = comrelay(rcvd1, con1, con2)
		if isNL == True: # new line
			text = "rcvd1," + rcvd1
			monsock.sendto(text, (monip, int(monport)))
			logger.add(text)
			rcvd1 = ""
		
		rcvd2,isNL = comrelay(rcvd2, con2, con1)
		if isNL == True:
			text = "rcvd2," + rcvd2
			monsock.sendto(text, (monip, int(monport)))
			logger.add(text)
			rcvd2 = ""

		rcvcmd,rcvd = recvCommand(cmdsock, rcvcmd)
		if rcvd == True and "\n" in rcvcmd:
			procCommand(rcvcmd)
			rcvcmd = ""

if __name__ == '__main__':
	main()

# TODO: 0m> fix for UDP fail when RPi2 does not get IP address > to work only COM relay
