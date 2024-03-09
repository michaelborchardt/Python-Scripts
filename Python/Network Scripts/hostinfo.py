#!/usr/bin/env python

import socket

def get_mach_info():
	host_name = socket.gethostname()
	ip_addr = socket.gethostbyname(host_name)
	print ("Host name: %s" %host_name)
	print ("Ip addr: %s" %ip_addr)
if __name__ == '__main__':
	get_mach_info()

