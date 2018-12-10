# -*- coding: utf-8 -*-
"""
Created on Fri May 18 12:33:29 2018

@author: prjve
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) 
#0 is no for udp and AF_Inet is used to determine we re using ip family and _DGRAM is used for imply datagram tranfer 

portno = 1234
ip = "192.168.43.3"

s.bind((ip, portno))
#bind fucntion takes tuple as argument


x = s.recvfrom(20)
data = x[0]
remoteip = x[1]
#20 imples only 20 bytes can be stored, it is known as buffer/box
print(data)
