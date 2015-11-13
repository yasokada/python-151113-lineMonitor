#import serial
import time
import socket

def procSetCommand(cmd1, cmd2, cmd3):
	return

def procCommand(rcvstr):
	print "rcvd:", rcvstr
	cmds = rcvstr.split(",")
	if "set" in cmds[0]:
		count = len(cmds)
		if count == 4:
			procSetCommand(cmds[1],cmds[2],cmds[3])	
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
