#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import sys

#python client.py localhost 12345 tcp_udp streaming 64

host = str(sys.argv[1])
port = int(sys.argv[2])
tcp_udp = str(sys.argv[3])
stop_stream = str(sys.argv[4])
size = int(sys.argv[5])


if tcp_udp == 'tcp':			#TCP 
	if stop_stream == 'stop':	#Stop
		print "RUNNING TCP STOP AND WAIT"
		'''
		startmsg, size = read();
		while (buf, size = read())
    	count += size
    	send(ackbuf, 1);
    	if (count >= expected_size)
        break;
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
		client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		client_sock.connect((host,port))
		client_sock.send(size)
		from_serv = client_sock.recv()
		print from_serv
		
else: 							#UDP
	if stop_stream == 'stop':	#stop
		print "RUNNING UDP STOP AND WAIT"
		'''
		startmsg, size = read();
		while (buf, size = read())
    	count += size
    	send(ackbuf, 1);
    	if (count >= expected_size)
        break;
		'''
	else:						#UDP stream
		print "RUNNING UDP STREAMING"
		'''
		'''