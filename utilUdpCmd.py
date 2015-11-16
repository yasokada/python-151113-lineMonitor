import time
import socket
from utilSetting import CSetting

# TODO: 1> error handling > cmd typo etc
# TODO: 1> recgonize the setting change (e.g. monip was changed to xxx) > not sure necessary or not

'''
v0.2 2015/11/13
  - add dummySerial.py
v0.1 2015/11/13
  - can get/set settings (monitor ip, monitor port, com delay[msec])
'''

s_setting = CSetting()

def getSetting():
	return s_setting

def procSetCommand(rcvstr):
	cmds = rcvstr.split(",")
	if "mon" in cmds[1]:
		count = len(cmds)
		if count == 4:
			s_setting.setMonip(cmds[2])
			s_setting.setMonport(cmds[3])
			print "set monitor (ip, port)"
			print s_setting.getMonip()
			print s_setting.getMonport()
	if "comdelay" in cmds[1]:
		s_setting.setComdelay(int(cmds[2]))
		print "set comdelay"
		print s_setting.getComdelay()

def procGetCommand(rcvstr):
	cmds = rcvstr.split(",")
	count = len(cmds)
	if count == 2:
		if "monip" in cmds[1]:
			print "monip," + s_setting.getMonip()
		if "monport" in cmds[1]:
			print "monport," + `s_setting.getMonport()`
		if "comdelay" in cmds[1]:
			print "comdelay," + `s_setting.getComdelay()`
	return

def procCommand(rcvstr):
	rcvstr = rcvstr.rstrip('\n')
	rcvstr = rcvstr.rstrip('\r')
	print "rcvd:[", rcvstr, "]"
	cmds = rcvstr.split(",")
	if "set" in cmds[0]:
		procSetCommand(rcvstr)
	if "get" in cmds[0]:
		procGetCommand(rcvstr)
	return

def recvCommand(cmdsock, rcvcmd):
	try:
		data,address = cmdsock.recvfrom(100)
	except socket.error:
		pass
	else:
		rcvcmd = rcvcmd + data
		return rcvcmd, True
	return rcvcmd, False

