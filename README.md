# Distributed Homework 4

The assignment is to determine the differences between TCP and UDP transport protocols, which will both use the stop and wait and pure streaming protocols to compare the differences between the two in speed when uploading 1GB of data.

##### Instructions to run
This requires Python version 3.x to run and consists of two python files, server and client.

Open two terminal windows and change directory to dshw4 for both terminals.
##### Terminal argument meaning:
**TCP transport protocol**: tcp
**UDP transport protocol**: udp
**Stop and Wait acknowledgement type**: stop
**Pure Streaming acknowledgement type**: stream
**Message Size**: ranging from 1 byte to 65,536 bytes, incrementing in powers of two (1, 2, 4, 8, 16, …)

**Server terminal** 

There are 3 arguments that must be entered for server.py to run correctly
```
$ python server.py [port_number] [transport_protocol] [acknowledgement_type]
```

hostname can be found by typing hostname in terminal, you will need this name in the client terminal later, so copy it on a notepad. This will give you the name of the server
```
$ hostname
```
First run the server file by typing this into terminal,
```
$ python server.py 12345 tcp stop
```

**Client terminal**
Client will require 5 arguments that must be entered for client.py to run correctly.

[hostname] will be the computer name that your client will be connecting to which is the server's name
**Terminal template to input arguments**
```
$ python client.py [hostname] [port_number] [transport_protocol] [acknowledgement] [message_size]
```
Then run the client file by typing this into terminal, let [hostname] be the host name of the machine that you wish to connect to
```
$ python client.py [hostname] 12345 tcp stop 1024
```