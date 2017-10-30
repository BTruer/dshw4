#!/usr/bin/expect -f

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12345 tcp stop > server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12345 tcp stop 1 > client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact


spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12345 tcp stop > server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12345 tcp stop 2 > client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12345 tcp stop > server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12345 tcp stop 4 > client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12345 tcp stop > server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12345 tcp stop 8 > client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12345 tcp stop > server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12345 tcp stop 16 > client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12345 tcp stop > server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12345 tcp stop 32 > client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@python.cs.rutgers.edu "python3 server.py 12345 tcp stop > server_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "python3 client.py python.cs.rutgers.edu 12345 tcp stop 64 > client_tcp_stop.txt;"
expect "assword:"
send "Karmayog!2\r"
interact
