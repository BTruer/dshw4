#!/usr/bin/expect -f

spawn ssh -t brt31@python.cs.rutgers.edu "cd dis/dshw4; python3 server.py 12345 tcp stop > server_tcp_stop.txt; python3 server.py 12345 tcp stop >> server_tcp_stop.txt"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "cd dis/dshw4;python3 client.py python.cs.rutgers.edu 12345 tcp stop 1 > client_tcp_stop.txt;exit"
expect "assword:"
send "Karmayog!2\r"
interact


spawn ssh brt31@python.cs.rutgers.edu "cd dis/dshw4;python3 server.py 12346 tcp stop >> server_tcp_stop.txt;exit"
expect "assword:"
send "Karmayog!2\r"
interact

spawn ssh brt31@prolog.cs.rutgers.edu "cd dis/dshw4;python3 client.py python.cs.rutgers.edu 12346 tcp stop 2 >> client_tcp_stop.txt;exit"
expect "assword:"
send "Karmayog!2\r"
interact
