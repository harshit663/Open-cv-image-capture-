# -*- coding: utf-8 -*-
"""
Created on Thu May 17 22:45:19 2018

@author: prjve
"""

import subproces
import getpass

username = input("Enter your username :- ")
password = getpass.getpass("Enter your password :- ")
app = input("Enter The program you want you use :- ")

login_status = subproces.getstatusoutput("sshpass -p {} ssh -o StrictHostChecking=false -l {} 192.168.43.3 -X {}".format(password, username, ))