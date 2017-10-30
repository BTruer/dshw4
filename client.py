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


#python client.py Toshtp 12345 tcp stop 1024
if tcp_udp == 'tcp':			#TCP 
	if stop_stream == 'stop':	#Stop
		print("RUNNING TCP STOP AND WAIT")
		total_size = 1073741824
		#sending
		client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		client_sock.connect((host,port))
		message = str(size)
		client_sock.send(message.encode('utf-8')) #sends message to server
		count = total_size
		buffer_ = ' '*size
		buffer_ = buffer_.encode('utf-8')
		message_count = 0
		total_amt_sent = 0
		start_time = time.time()				#grab start time
		while(count>0):							#while count is still bigger then 0 (it should be approching 0)
			amt_sent = client_sock.send(buffer_) #send the buffer to the server and get the amtsend
			total_amt_sent += amt_sent 	 		#increment the amount sent
			if(amt_sent < size):				#if the amount sent is less then the size it should be sending
				print("ERROR: Amount sent was less then the buffer size")
			count -= amt_sent 						#decrease count by the amount sent
			message_count+=1					#message counter
			ack=client_sock.recv(1024).decode()
		stop_time = time.time()					#done grab time
		print("number of messages sent:"+str(message_count))
		print("number of bytes sent:"+str(total_amt_sent))
		diff = stop_time - start_time
		print("time took:" + str(diff))
		client_sock.close()
	
	else:#python client.py Toshtp 12345 tcp streaming 16000
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
		server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #create a tcp socket
		server_sock.connect((host,port))   #connect hte socket to the remote host machine at port
		total_size = 1073741824 			#the size of 1 GB
		message =  "message_size:"+str(size) #send the message size to the server
		server_sock.send(message.encode('utf-8')) 	#send the size
		count = total_size						#count is 1GB --will go to 0
		buffer_ = ' '*size  					#buffer of data
		buffer_ = buffer_.encode('utf-8')		#encode the data to send over the socket
		message_count = 0						#keep the message count
		total_amt_sent = 0						#keep the amount sent count
		ack = server_sock.recv(1024).decode()	#get an ok (1) from the server
		start_time = time.time()				#grab start time
		while(count>0):							#while count is still bigger then 0 (it should be approching 0)
			amt_sent = server_sock.send(buffer_) #send the buffer to the server and get the amtsend
			total_amt_sent += amt_sent 	 #increment the amount sent
			if(amt_sent < size):				#if the amount sent is less then the size it should be sending
				print("ERROR: Amount sent was less then the buffer size")
			count -= amt_sent 						#decrease count by the amount sent
			message_count+=1					#message counter
		stop_time = time.time()					#done grab time
		print("number of messages sent:"+str(message_count))
		print("number of bytes sent:"+str(total_amt_sent))
		diff = stop_time - start_time
		print("time took:" + str(diff))
		server_sock.close()
		
else: 							#UDP
	if stop_stream == 'stop':	#stop
		print("RUNNING UDP STOP AND WAIT")
		'''
		1G = 2^30
		1M = 2^20
		need_ack, msg_size = read_from_cmd_line()
		startmsg = { need_ack=1, total_size=1G }
		send(startmsg)
		count = total_size
		start_time = start_timer()
		while (count > 0)
			bytes_sent = send(buffer, msg_size)
			if (bytes_sent != msg_size)
				error()
			count -= bytes_sent 
			ack, bytes_read = read()
		stop_time = stop_timer()
		print (stop_time - start_time)/1M   # throughput in megabytes per second

		'''
		total_size = 1073741824
		message = str(size)
		#sending
		client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		client_sock.sendto(message.encode('utf-8'),(host,port))
		count = total_size
		buffer_ = ' '*size
		buffer_ = buffer_.encode('utf-8')
		message_count = 0
		total_amt_sent = 0
		
		start_time = time.time()				#grab start time
		while(count>0):							#while count is still bigger then 0 (it should be approching 0)
			amt_sent = client_sock.sendto(buffer_,(host,port)) #send the buffer to the server and get the amtsend
			total_amt_sent += amt_sent 	 		#increment the amount sent
			if(amt_sent < size):				#if the amount sent is less then the size it should be sending
				print("ERROR: Amount sent was less then the buffer size")
			count -= amt_sent 						#decrease count by the amount sent
			message_count+=1					#message counter
			ack, serverAddress=client_sock.recvfrom(1024)
			ack=ack.decode()
		stop_time = time.time()					#done grab time
		print("number of messages sent:"+str(message_count))
		print("number of bytes sent:"+str(total_amt_sent))
		diff = stop_time - start_time
		print("time took:" + str(diff))
		
		client_sock.close()



	else:#python client.py Toshtp 12345 udp streaming 1024						#UDP stream
		print("RUNNING UDP STREAMING")
		'''
		1G = 2^30
		1M = 2^20
		need_ack, msg_size = read_from_cmd_line()
		startmsg = { need_ack=0, total_size=1G }
		send(startmsg)
		count = total_size
		start_time = start_timer()
		while (count > 0)
		    bytes_sent = send(buffer, msg_size)
		    if (bytes_sent != msg_size)
		        error()
		    count -= bytes_sent 
		stop_time = stop_timer()
		print (stop_time - start_time)/1M   # throughput in megabytes per second
		'''
		server_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		server = (host,port)
		server_sock.connect(server)
		total_size = 1073741824 			#the size of 1 GB
		message =  "message_size:"+str(size) #send 1GB and the message size to the server
		server_sock.sendto(message.encode('utf-8'), server)
		count = total_size
		buffer_ = ' '*size
		buffer_ = buffer_.encode('utf-8')
		message_count = 0
		total_amt_sent = 0
		start_time = time.time()
		while(count>0):
			amt_sent = server_sock.sendto(buffer_, server)
			total_amt_sent += amt_sent
			if(amt_sent < size):				#if the amount sent is less then the size it should be sending
				print("ERROR: Amount sent was less then the buffer size")
			count -= amt_sent 						#decrease count by the amount sent
			message_count+=1
		stop_time = time.time()
		print("number of messages sent:"+str(message_count))
		print("number of bytes sent:"+str(total_amt_sent))
		diff = stop_time - start_time
		print("time took:" + str(diff))
		server_sock.close()