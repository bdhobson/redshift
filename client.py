#!/usr/bin/python

import socket
import os

ports = [ 80, 443, 12345 ]

s = socket.socket()
host = socket.gethostname()

MAX_TRANSMISSION_SIZE = 1024 * 1024
print "size", MAX_TRANSMISSION_SIZE

for port in ports:
	print "Connecting to port", port
	try:
		s.connect((host, port))
		print s.recv(1024)
		s.send('TCP data block')
#		f = open('/etc/passwd', 'rb')
#		l = 64 + f.read(64)
		l = os.urandom(MAX_TRANSMISSION_SIZE)
		i = 0
		while (l and i < 10):
			print 'Sending...', len(l), " ", i
			s.send(l)
			l = os.urandom(MAX_TRANSMISSION_SIZE)
			i = i + 1
#			l = f.read(64)
#		f.close()
		#s.sendto('UDP data block')
#		s.shutdown(socket.SHUT_WR)
		s.close()
	except socket.error:
		print "Port", port, "not open"
#	else:
#		print "unknown error"

