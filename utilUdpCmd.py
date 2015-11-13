import time
import socket
from utilSetting import CSetting

g_setting = CSetting()

# TODO: 1> error handling > cmd typo etc
# TODO: 0c> add utilCom.py > COM relay feature
# TODO: 0m> move main() to linemonitor.py
# TODO: 1> can recgonize the setting change (e.g. monip was changed to xxx)
# TODO: 0z> python > static function in a Class

'''
v0.2 2015/11/13
  - add dummySerial.py
v0.1 2015/11/13
  - can get/set settings (monitor ip, monitor port, com delay[msec])
'''

def procSetCommand(rcvstr):
	cmds = rcvstr.split(",")
	if "mon" in cmds[1]:
		count = len(cmds)
		if count == 4:
			g_setting.setMonip(cmds[2])
			g_setting.setMonport(cmds[3])
			print "set monitor (ip, port)"
			print g_setting.getMonip()
			print g_setting.getMonport()
	if "comdelay" in cmds[1]:
		g_setting.setComdelay(int(cmds[2]))
		print "set comdelay"
		print g_setting.getComdelay()

def procGetCommand(rcvstr):
	cmds = rcvstr.split(",")
	count = len(cmds)
	if count == 2:
		if "monip" in cmds[1]:
			print "monip," + g_setting.getMonip()
		if "monport" in cmds[1]:
			print "monport," + `g_setting.getMonport()`
		if "comdelay" in cmds[1]:
			print "comdelay," + `g_setting.getComdelay()`
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

def main():
	cmdip = ""
	cmdport = 7000
	cmdsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	cmdsock.bind((cmdip, cmdport))
	cmdsock.setblocking(0)

	rcvcmd = ""

	while 1:
		rcvcmd,rcvd = recvCommand(cmdsock, rcvcmd)
		if rcvd == True and "\n" in rcvcmd:
			procCommand(rcvcmd)
			rcvcmd = ""

if __name__ == '__main__':
	main()
