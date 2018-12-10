# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:53:35 2018

@author: prjve

"""

import subprocess
import getpass


def setup_xwindow():
    print("Setting up X11Forwarding...")
    xwin_output = subprocess.getstatusoutput("grep -i x11forwarding /etc/ssh/sshd_config | grep -v '#'")
    if 'no' in xwin_output[1]:
        x_output = subprocess.getstatusoutput("sed -i 's/X11Forwarding no/X11Forwarding yes/' /etc/ssh/sshd_config")
        if x_output[0] == 0:
            print("X11Forwarding is set up")
    else:
        print("X11Forwarding is set up")
    
def ssh_service_service():
    subprocess.getoutput("systemctl restart sshd")
    service_out = subprocess.getstatusoutput("systemctl is-active sshd")
    if service_out[1] == 'active':
        print("ssh service started...")
    else:
        print("ssh service is stopped...")
        
def user_create():
    uname = input("Enter your username :- ")
    user_status = subprocess.getstatusoutput("useradd {}".format(uname))
    if user_status[0] == 0:
        print("User {} created sucessfully".format(uname))
    else:
        print("Error in creating user or user exists")
        
    upass = getpass.getpass("Enter the password for {}".format(uname))
    pass_status = subprocess.ggetstatusoutput("echo {} | passwd {} --stdin".format(upass, uname))
    if pass_status[0] == 0:
        print("Password changed sucessfully")
    else:
        print("Error in changing password")
        
        