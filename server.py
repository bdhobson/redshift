#!/usr/bin/python

# spawn connection threads
# keep metrics by connecting ip address
# keep metrics by successful ports
# timing/amount of data collected
# storage? sqlite, python db interface?

import socket
import thread
import time

host = socket.gethostname()

def client_session(threadName, socket):
	print "Running client_session"
	socket.send('Thank you for connecting')
	print socket.recv(1024)
#	time.sleep(5)
#	socket.close()

	f = open('recv.log', 'wb')
	l = socket.recv(1024)
	while(l):
		print "Receiving..."
		f.write(l)
		l = socket.recv(1024)
	f.close()
	

def port_listener(threadName, port):
	s = socket.socket()
	s.bind((host, port))
	s.listen(5)
	while True:
		c, addr = s.accept()
		print 'Got a connection from', addr
		thread.start_new_thread( client_session, ("thread-1", c) )
		

try:
	thread.start_new_thread( port_listener, ("thread-1", 12345) )
except:
	print "Error spawning thread for port", 12345

while 1:
	pass

