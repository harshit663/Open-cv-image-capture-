# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:24:24 2018

@author: prjve
"""

import subprocess

print("Creating LVM...")
def create_pv():
    print("Creating Physical volume 1...")
    pv1_out = subprocess.getstatusoutput('echo y | pvcreate /dev/sdb1')
    if pv1_out[0] == 0:
        print("Physical Volume 1 created sucessfully")
    else:
        print("Error in creating Physical volume 1")
    print(subprocess.getoutput('pvdisplay /dev/sdb1'))
    print("Creating Physical volume 2...")
    pv2_out = subprocess.getstatusoutput('echo y | pvcreate /dev/sdc1')
    if pv2_out[0] == 0:
        print("Physical Volume 2 created sucessfully")
    else:
        print("Error in creating Physical volume 2")
    print(subprocess.getoutput('pvdisplay /dev/sdc1'))
    

def create_vg():
    print("Creating Volume group...")
    vg_out = subprocess.getstatusoutput('vgcreate myvg /dev/sdb1 /dev/sdc1')
    if vg_out[0] == 0:
        print("Volume Group created sucessfully")
    else:
        print("Error in creating Volume Group")
    print(subprocess.getoutput('vgdisplay myvg'))
    
def create_lv():
    print("Creating Logical volume...")
    lv_out =  subprocess.getstatusoutput('lvcreate --name mylv --size 20G myvg')
    if lv_out[0] == 0:
        print("Logical volume created sucessfully")
    else:
        print("Error in creating Logical volume")
    print(subprocess.getoutput('lvdisplay /dev/myvg/mylv'))
    print("Formatting the Logical volume PLEASE WAIT...")
    lv_format = subprocess.getstatusoutput('mkfs.ext4 /dev/myvg/mylv')
    if lv_format[0] == 0:
        print("Logical volume formatted successfully")
    else:
        print("Error in creating Logical volume")
    print("Creating Drive...")
    subprocess.getoutput('mkdir /media/mydrive')
    subprocess.getoutput('mount /dev/myvg/mylv  /media/mydrive')
   
    
def undo_lvm():
    print("Reoving Logical volume...")
    subprocess.getoutput('umount /media/mydrive')
    lv_remove = subprocess.getstatusoutput('echo y | lvremove /dev/myvg/mylv')
    if lv_remove[0] == 0:
        print("Logocal volume removed sucessfully")
    else:
        print("Error in removing Logical volume")
    print("Removing Volume group...")
    subprocess.getoutput('vgremove myvg')
    print("Removing Physical volume...")
    subprocess.getoutput('pvremove /dev/sdb1')
    subprocess.getoutput('pvremove /dev/sdc1')
    
    
def extend_vg():
    subprocess.getoutput('vgextend myvg /dev/sde1')
    
def extend_lv():
    print("Increasing Logical volume...")
    lv_extend = subprocess.getstatusoutput('lvextend --size +1G /dev/myvg/mylv')
    if lv_extend[0] == 0:
        print("Logical Volume Extended")
    else:
        print("Error in extending Logical Volume")
    print("Wraping up...")
    resize = subprocess.getstatusoutput('resize2fs /dev/myvg/mylv')
    if resize[0] == 0:
        print("Done")
    else:
        print("Error in Resizing")
    print(subprocess.getoutput("lvdisplay /dev/myvg/mylv"))
    
    
#create_pv()
#create_vg()
#create_lv()
#extend_lv()
undo_lvm()