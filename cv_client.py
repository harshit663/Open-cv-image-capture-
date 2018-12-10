# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 08:56:44 2018

@author: prjve
"""

import cv2
import socket

s = socket.socket()

ip = "192.168.43.120"    # Receiver's IP
port = 3333

s.connect((ip, port))

d = s.recv(1024)
print(d.decode())

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        cv2.imwrite("img.jpg", frame)
        imgf = open('img.jpg', 'rb')
        data = imgf.read()

        s.send(data)
        s.send(b'end')

        imgf.close()
s.close()