from utilUdpCmd import recvCommand, procCommand
from utilSetting import CSetting
import socket

# TODO: 1> something does not sit right concerning setting passing (g_setting)

g_setting = CSetting()

def main():
	cmdip = ""
	g_setting = CSetting()
	cmdport = g_setting.getCmdPort()
	cmdsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	cmdsock.bind((cmdip, cmdport))
	cmdsock.setblocking(0)

	print "cmdport=", cmdport

	rcvcmd = ""

	while 1:
		rcvcmd,rcvd = recvCommand(cmdsock, rcvcmd)
		if rcvd == True and "\n" in rcvcmd:
			procCommand(rcvcmd)
			rcvcmd = ""

if __name__ == '__main__':
	main()
