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

#python client.py Toshtp 12345 tcp stop 1024
if tcp_udp == 'tcp':			#TCP 
	if stop_stream == 'stop':	#Stop
		print("RUNNING TCP STOP AND WAIT")
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


	else:#python client.py Toshtp 12345 tcp streaming 1024
		print("RUNNING TCP STREAMING")
		'''
		1G = 2^30
		1M = 2^20
		need_ack, msg_size = read_from_cmd_line() 	done 
		startmsg = { need_ack=0, total_size=1G } 	done
		send(startmsg) 								done
		count = total_size done						done
		start_time = start_timer()					done
		while (count > 0)
		    bytes_sent = send(buffer, msg_size)
		    if (bytes_sent != msg_size)
		        error()
		    count -= bytes_sent 
		stop_time = stop_timer()
		print (stop_time - start_time)/1M   # throughput in megabytes per second
		'''
		server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		server_sock.connect((host,port))
		total_size = 1073741824
		message =  "total_size:"+str(total_size)+",message_size:"+str(size)
		server_sock.send(message.encode('utf-8')) 	#send the size
		count = total_size
		buffer_ = ' '*size
		message_count = 0
		total_amt_sent = 0
		ack = server_sock.recv(1024)
		if ack == 1:
			print("ack. received beginning")
		start_time = time.time()
		while(count>0):
			amt_sent = server_sock.send(buffer_)
			total_amt_sent += amt_sent
			if(amt_sent < size):
				print("ERROR: Amount sent was less then the buffer size")
				count-= amt_sent
			else:
				count -= size
			message_count+=1
		stop_time = time.time()
		print("number of messages sent:"+message_count)
		print("number of bytes sent:"+total_amt_sent)
		diff = stop_time - start_time

		print("time took:" + diff)
		server_sock.close()
		
else: 							#UDP
	if stop_stream == 'stop':	#stop
		print("RUNNING UDP STOP AND WAIT")
		'''
		send(startmsg)
		ack, size = read()
		while (count > 0)
    		send(buffer, size)
    		count -= size
		'''
	else:						#UDP stream
		print("RUNNING UDP STREAMING")
		'''
		'''