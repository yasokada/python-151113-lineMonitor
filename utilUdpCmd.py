#import serial
import time
import socket

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
			print "rcvd command=",rcvcmd
			rcvcmd = ""

if __name__ == '__main__':
	main()
