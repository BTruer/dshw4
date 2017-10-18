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
		

	else:						#TCP stream
		print "RUNNING TCP STREAMING"
		'''
		startmsg, size = read()
		send(ackbuf, 1)  *
		while (buf, size = read())
    		count += size
    		if (count >= expected_size)
        		break
		'''
		server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
		host = socket.gethostname() # Get local machine name
		server_sock.bind((host, port))        # Bind to the port
		server_sock.listen(5)
		while True:
		   client_sock, addr = server_sock.accept()     # Establish connection with client.
		   startmsg_size = client_sock.recv()
		   print startmsg_size
		   client_sock.send('Thank you for connecting')
		   client_sock.close()    

else: 							#UDP
	if stop_stream == 'stop':	#stop
		print "RUNNING UDP STOP AND WAIT"
		
	else:						#UDP stream
		print "RUNNING UDP STREAMING"
		