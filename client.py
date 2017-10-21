#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import sys

#python client.py Toshtp 12345 tcp_udp streaming 64

host = str(sys.argv[1])
port = int(sys.argv[2])
tcp_udp = str(sys.argv[3])
stop_stream = str(sys.argv[4])
size = int(sys.argv[5])


if tcp_udp == 'tcp':			#TCP 
	if stop_stream == 'stop':	#Stop
		print "RUNNING TCP STOP AND WAIT"
		'''
		'''

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