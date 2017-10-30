#!/usr/bin/expect -f

spawn ssh brt31@python.cs.rutgers.edu "echo thisisbt;exit"
expect "assword:"
send "Karmayog!2\r"
interact