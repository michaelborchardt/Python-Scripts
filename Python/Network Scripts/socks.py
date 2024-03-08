#!/usr/bin/env python
import socket

def fsn():
	protoname = 'tcp'
	for port in [80, 25, 22]:
		print ("Port: %s => service name %s" %(port, socket.getservbyport(port, protoname)))
if __name__ == '__main__':
	fsn()

