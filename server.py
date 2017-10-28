#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import sys

#python server.py 12345 tcp stop
port = int(sys.argv[1])
tcp_udp = str(sys.argv[2])
stop_stream = str(sys.argv[3])

if tcp_udp == 'tcp':			#TCP 
	if stop_stream == 'stop':	#Stop
		print("RUNNING TCP STOP AND WAIT")
		'''
		startmsg, size = read();
		while (buf, size = read())
			count += size
			send(ackbuf, 1);
			if (count >= expected_size)
				break
		'''
		expected_size= 1073741824
		server_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		host = socket.gethostname()
		print("this is host name: "+str(host))
		server_sock.bind((host,port))
		server_sock.listen(5)
		to_client_sock, addr = server_sock.accept()
		temp = to_client_sock.recv(1024)
		message_size=int(temp)
		print("recieved:"+str(message_size))
		count=0

		#while you can still recieve
		while True:
			data = to_client_sock.recv(message_size).decode()
			count+=len(data)
			print("this is current count: "+str(count))
			to_client_sock.send('1'.encode())
			if(count>=expected_size):
				break
		print("num of bytes read:"+str(count))	
		to_client_sock.close() 


	else:#python server.py 12345 tcp stream #TCP stream
		print("RUNNING TCP STREAMING")
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
		temp = client_sock.recv(1024).decode().split(',')
		total_size = int(temp[0].split(":")[1])
		message_size = int(temp[1].split(":")[1])
		client_sock.send('1'.encode())					# Send the ack bit
		byte_count = 0
		messages = 0
		while True:
			data = client_sock.recv(message_size).decode()
			byte_count += len(data)
			messages+=1
			if(byte_count >= total_size):
				break
		print("num of messages read:"+str(messages))
		print("num of bytes read:"+str(byte_count))

		client_sock.close()    

else: 							#UDP
	if stop_stream == 'stop':	#stop
		print("RUNNING UDP STOP AND WAIT")
		'''
		'''
		expected_size= 1073741824
		server_sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		host = socket.gethostname()
		print("this is host name: "+str(host))
		server_sock.bind((host,port))
		
		temp, clientAddress = server_sock.recvfrom(1024)
		print("recieved temp:"+ temp)
		message_size=int(temp)
		print("recieved:"+str(message_size))
		count=0

		#while you can still recieve
		
		while True:
			data, clientAddress = server_sock.recvfrom(message_size)
			data=data.decode()
			count+=len(data)
			print("this is current count: "+str(count))
			server_sock.sendto('1'.encode(), clientAddress)
			if(count>=expected_size):
				break
		print("num of bytes read:"+str(count))	
		server_sock.close() 
	else:						#UDP stream
		print("RUNNING UDP STREAMING")
		'''
		
		server_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
		host = socket.gethostname()
		client = (host, port) 			# Get local machine name
		server_sock.bind(client) 			# Bind to the port
		while True:
			data, address = sock.recvfrom(4096)
		'''