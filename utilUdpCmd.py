#import serial
import time
import socket
import utilSetting
from utilSetting import CSetting

g_setting = CSetting()

def procCommand(rcvstr):
	rcvstr = rcvstr.rstrip('\n')
	rcvstr = rcvstr.rstrip('\r')
	print "rcvd:[", rcvstr, "]"
	cmds = rcvstr.split(",")
	if "set" in cmds[0]:
		if "mon" in cmds[1]:
			count = len(cmds)
			if count == 4:
				print "set monitor (ip, port)"
		if "comdelay" in cmds[1]:
			g_setting.setComdelay(int(cmds[2]))
			print "set comdelay"
			print g_setting.getComdelay()

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
