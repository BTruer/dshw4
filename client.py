#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import sys
import time

#python client.py Toshtp 12345 tcp_udp streaming 64

host = str(sys.argv[1])
port = int(sys.argv[2])
tcp_udp = str(sys.argv[3])
stop_stream = str(sys.argv[4])
size = int(sys.argv[5])
count = 1073741824


if tcp_udp == 'tcp':			#TCP 
	if stop_stream == 'stop':	#Stop
		print "RUNNING TCP STOP AND WAIT"
		'''
		'''
		startmessage=' '*size

		client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		client_sock.connect((host,port))
		client_sock.send(str(size))
		ack = client_sock.recv(1024) 

		#start message sends the total amount of data to be transfered
		#buffer is just empty bytes could be anything
		#buffersize this is the specified by the client from the command line
		send(startessage size)
		i meant to say recv grabs the first guy then the second guy?
		startmessage=recv(1024)
		size=recv(1024)


	else:#python client.py Toshtp 12345 tcp streaming 65536  #TCP stream
		print "RUNNING TCP STREAMING"
		'''
		send(startmsg)     		done 
		ack, size = read()		done
		while (count > 0)		
    		send(buffer, size)
    		count -= size
		'''
		server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		server_sock.connect((host,port))
		server_sock.send(str(size)) 	#send the size
		ack = server_sock.recv(1024) 	#get the ack bit
		count = 0
		while(count>0):
			server_sock.send(' '+str())
		server_sock.close()

else: 							#UDP
	if stop_stream == 'stop':	#stop
		print "RUNNING UDP STOP AND WAIT"
		'''
		send(startmsg)
		ack, size = read()
		while (count > 0)
    		send(buffer, size)
    		count -= size
		'''
	else:						#UDP stream
		print "RUNNING UDP STREAMING"
		'''
		'''