# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:35:29 2018

@author: prjve
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

ip = "192.168.43.3"
port = 2222

print('''
1. To create cloud 
2. To create hadoop
3. create user
4. Exit    
''')

ch = int(input("Enter your choice :- "))

if ch == 1:
    print("Cloud")
elif ch == 2:
    print('hadoop')
elif ch == 3:
    name = input("Enter user name :-")
    print("Hello {}".format(name))
    name = name.encode('utf-8')
    s.sendto(name, (ip, port))
else:
    print("Invalid option")