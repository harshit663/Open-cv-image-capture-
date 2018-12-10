# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 08:23:37 2018

@author: prjve
"""

import cv2
#import subprocess as sp
import socket

s = socket.socket()
ip = ""
port = 3333

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)

s.bind((ip, port))

s.listen(5)
con1, addr = s.accept()
st = "Welcome"
st = st.encode('utf-8')
con1.send(st)

while True:
    fname = 'image' + '.jpg'
    f1 = open(fname, 'wb')
    while True:
        idata = con1.recv(2048)
        
        if(b'end' in idata):
            idata = idata[:idata.find(b'end')]
            f1.write(idata)
            break 
        
        f1.write(idata)			# Write the received image to the opened file
	
    f1.close()				# Close the file

    try:					# Try block will avoid any errors and continue displaying video
        img = cv2.imread(fname)
        cv2.imshow('img', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except:
        continue

con1.close()
s.close()
        
        
        
