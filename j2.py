#!/usr/bin/python
import socket
hst = socket.gethostname()
ip = socket.gethostbyname(hst)

print '{0}  {1}'.format(hst,ip)
