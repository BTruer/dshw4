#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import sys

#python server.py 12345 tcp stop
port = int(sys.argv[1])
tcp_udp = str(sys.argv[2])
stop_stream = str(sys.argv[3])
print port, tcp_udp, stop_stream


if tcp_udp == 'tcp':			#TCP 
	if stop_stream == 'stop':	#Stop
		print "RUNNING TCP STOP AND WAIT"
		'''
		send(startmsg);
		ack, size = read();
		while (count > 0)
    	send(buffer, size);
    	count -= size;
    	ack, size = read();
		'''

	else:						#TCP stream
		print "RUNNING TCP STREAMING"
		'''
		send(startmsg)
		ack, size = read()
		while (count > 0)
    	send(buffer, size)
    	count -= size
		'''
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
		host = socket.gethostname() # Get local machine name
		s.bind((host, port))        # Bind to the port
		s.listen(5)
		while True:
		   c, addr = s.accept()     # Establish connection with client.
		   print 'Got connection from', addr, 'number of bytes sent', c
		   c.send('Thank you for connecting')
		   c.close()    

else: 							#UDP
	if stop_stream == 'stop':	#stop
		print "RUNNING UDP STOP AND WAIT"
		'''
		send(startmsg);
		ack, size = read();
		while (count > 0)
	    send(buffer, size);
	    count -= size;
	    ack, size = read();
		'''
	else:						#UDP stream
		print "RUNNING UDP STREAMING"
		'''
		send(startmsg)
		ack, size = read()
		while (count > 0)
    		send(buffer, size)
    		count -= size
		'''