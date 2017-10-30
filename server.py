#!/usr/bin/python3           # This is server.py file

import socket               # Import socket module
import sys


port = int(sys.argv[1])
tcp_udp = str(sys.argv[2])
stop_stream = str(sys.argv[3])

if tcp_udp == 'tcp':#python server.py 12345 tcp stop  
	if stop_stream == 'stop': #TCP Stop
		print("RUNNING TCP STOP AND WAIT")
		expected_size= 1073741824
		server_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		host = socket.gethostname()
		server_sock.bind((host,port))
		server_sock.listen(5)
		to_client_sock, addr = server_sock.accept()
		temp = to_client_sock.recv(1024)
		message_size=int(temp)
		count = 0
		messages = 0
		#while you can still receive
		while True:
			data = to_client_sock.recv(message_size).decode()
			count+=len(data)
			messages+=1
			to_client_sock.send('1'.encode())
			if(count>=expected_size):
				break
		print("num of bytes read:"+str(count))	
		print("num of messages read:"+str(messages))	
		to_client_sock.close() 


	else:#python server.py 12345 tcp stream #TCP stream
		print("RUNNING TCP STREAMING")
		server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
		host = socket.gethostname() 			# Get local machine name
		server_sock.bind((host, port)) 			# Bind to the port
		server_sock.listen(5)					# Get to listen
		client_sock, addr = server_sock.accept()# Establish connection with client
		message_size = int(client_sock.recv(1024).decode().split(':')[1])  #recieve the message size from the server
		client_sock.send('1'.encode())					# Send the ack bit
		total_size = 1073741824
		byte_count = 0
		messages = 0
		while True:
			data = client_sock.recv(message_size).decode()
			byte_count += len(data)
			messages+=1
			if(byte_count >= total_size):
				break
		print("num of bytes read:"+str(byte_count))
		print("num of messages read:"+str(messages))
		client_sock.close()    

else:#python server.py 12345 udp stop 
	if stop_stream == 'stop': #UDP stop
		print("RUNNING UDP STOP AND WAIT")
		expected_size = 1073741824
		server_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		host = socket.gethostname()
		server_sock.bind((host,port))
		temp, clientAddress = server_sock.recvfrom(1024)
		temp = temp.decode()
		message_size = int(temp)
		count = 0
		messages = 0
		#while you can still receive
		while True:
			data, clientAddress = server_sock.recvfrom(message_size)
			data = data.decode()
			count += len(data)
			messages+=1
			server_sock.sendto('1'.encode(), clientAddress)
			if(count >= expected_size):
				break
		print("num of bytes read:"+str(count))
		print("num of messages read:"+str(messages))	
		server_sock.close() 
	else:#python server.py 12345 udp streaming						#UDP stream
		print("RUNNING UDP STREAMING")
		expected_size = 1073741824
		server_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
		host = socket.gethostname()
		client = (host, port) 			# Get local machine name
		server_sock.bind(client) 			# Bind to the port
		temp, clientAddress = server_sock.recvfrom(1024)
		message_size = int(temp.decode().split(':')[1])
		count = 0
		messages = 0
		while True:
			data, address = server_sock.recvfrom(message_size)
			data=data.decode()
			count+=len(data)
			messages+=1
			if(count>=expected_size):
				break
		print("num of bytes read:"+str(count))
		print("num of messages read:"+str(messages))
		server_sock.close()