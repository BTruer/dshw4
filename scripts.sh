#!/usr/bin/expect -f

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12345 tcp stop > server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12345 tcp stop 1 > client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact


spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12346 tcp stop >> server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12346 tcp stop 2 >> client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12347 tcp stop >> server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12347 tcp stop 4 >> client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12348 tcp stop >> server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12348 tcp stop 8 >> client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12349 tcp stop >> server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12349 tcp stop 16 >> client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12350 tcp stop >> server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12350 tcp stop 32 >> client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12351 tcp stop >> server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12351 tcp stop 64 >> client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12352 tcp stop >> server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12352 tcp stop 128 >> client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12353 tcp stop >> server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12353 tcp stop 256 >> client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12354 tcp stop >> server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12354 tcp stop 512 >> client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12355 tcp stop >> server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12355 tcp stop 1024 >> client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12355 tcp stop >> server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12356 tcp stop 2048 >> client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 123456 tcp stop >> server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12357 tcp stop 4096 >> client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12357 tcp stop >> server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12358 tcp stop 8192 >> client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12358 tcp stop >> server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12359 tcp stop 16384 >> client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12359 tcp stop >> server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12360 tcp stop 32768 >> client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12360 tcp stop >> server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12345 tcp stop 65536 >> client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact