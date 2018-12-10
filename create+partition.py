# -*- coding: utf-8 -*-
"""
Created on Fri May 18 11:53:53 2018

@author: prjve
"""

import subprocess

def create():
    drive_name = input("Enter the name of the hard drive :- ")
    size = input("Size of the partion that you want to make in (K/M/G):- ")
    part_out = subprocess.getstatusoutput("echo -e 'n\np\n\n\n+{}\nw\n' | fdisk {}".format(size, drive_name))
    if part_out[0] == 0:
        print("Partition created sucessfully")
    else:
        print("Error in creating partition ")
        
create()

if __name__ == '__main__':
    print("\t\t\tWelcome to the world of partitioning :- ")
    print('''
1: Create Partition
2: Delete Partition
3  Extend Partition        
''')
    