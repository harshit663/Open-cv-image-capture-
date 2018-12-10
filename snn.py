# -*- coding: utf-8 -*-
"""
Created on Thu May 31 20:32:14 2018

@author: prjve
"""

import subprocess as sp
import time

print("Welcome")
print("Checking...")
def check_master():
    time.sleep(1)
    x = True
    while x:
        time.sleep(1)
        pingout = sp.getstatusoutput("ping -c 2 10.0.0.2")
        if pingout[0] == 1:
            print("Cant connect to network, Checking again...")
            time.sleep(1)
            ping1out = sp.getstatusoutput("ping -c 2 10.0.0.2")
            if ping1out == 1:
                ipout = sp.getstatusoutput("ifconfig enp0s3 192.168.43.3")
                if ipout[0] == 0:
                    print("IP changed success.")
                had = sp.getstatusoutput("hadoop-daemon.sh start namenode")
                if had[0] == 0:
                    print("Service started successfully")
                else:
                    print("Service couldn't start")
                
            
        
