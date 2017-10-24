#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import sys

#python server.py 12345 tcp stop
port = int(sys.argv[1])
tcp_udp = str(sys.argv[2])
stop_stream = str(sys.argv[3])

if tcp_udp == 'tcp':			#TCP 
	if stop_stream == 'stop':	#Stop
		print "RUNNING TCP STOP AND WAIT"
		'''
		'''

	else:#python server.py 12345 tcp stream #TCP stream
		print "RUNNING TCP STREAMING"
		'''
		ack, size = read()
		send(ackbuf, 1)
		while (buf, bytes_read = read())
		    count += bytes_read
		    if (count >= expected_size)
		        break
		'''
		server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
		host = socket.gethostname() 			# Get local machine name
		server_sock.bind((host, port)) 			# Bind to the port
		server_sock.listen(5)					# Get to listen
		client_sock, addr = server_sock.accept()# Establish connection with client
		buff_size = int(client_sock.recv(1024))	# Get the buffer size
		client_sock.send('1')					# Send the ack bit
		count = 0
		while True:
			data, size = client_sock.recv(buff_size).split(,)
			count += size
			if(count >= buff_size)
				break

		client_sock.close()    

else: 							#UDP
	if stop_stream == 'stop':	#stop
		print "RUNNING UDP STOP AND WAIT"
		'''
		'''
	else:						#UDP stream
		print "RUNNING UDP STREAMING"
		'''
		'''