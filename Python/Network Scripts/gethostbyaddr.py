#!/usr/bin/env python
import socket

print(format('-','-<30'), ' Get Host By Address ', format('-','->30'))
name = input('What is host address: ')
sock = socket.gethostbyaddr(name)
print('Getting hostname:', sock)