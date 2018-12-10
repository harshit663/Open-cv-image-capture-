import subprocess as s

def part():
   y=s.getstatusoutput("fdisk -l | grep /dev")
   print(y[1])
   print("enter drive name from above which you want to partition (eg: /dev/sdb)")
   drive_name=input()
   d_part=s.getstatusoutput("echo -e 'p\nd\nn\np\n\n\n\nw\n' |fdisk {}".format(drive_name))
   print(d_part)
   if d_part[0]==0:
      partprobe=s.getstatusoutput("partprobe {}".format(drive_name))
   else:
      print("error")

def del_p():
   y=s.getstatusoutput("fdisk -l | grep /dev")
   print(y[1])
   print("enter drive name from above from which you want to delete partition (eg: sdb)")
   drive_name=input()
   y=s.getstatusoutput("lsblk | grep {}".format(drive_name))
   print("you have following drives and partition in drive {}".format(drive_name))
   print(y[1])
   print("select partition number from drive {} which you you want to delete".format(drive_name))
   p_no=(int)(input())
   part=s.getstatusoutput("echo -e 'p\nd\n{}\nw\n' | fdisk /dev/{}".format(p_no,drive_name))
   if part[0]==0:
        s.partprobe=s.getstatusoutput("partprobe /dev/{}".format(drive_name))
        print("partition deleted successfully")
   else:
        print ("error")


def part1():
   y=s.getstatusoutput("fdisk -l | grep /dev")
   print(y[1])
   print("enter drive name from above which you want to partition (eg: sdb)")
   drive_name=input()
   print("partition already present in drive {}".format(drive_name))
   drive_list=s.getstatusoutput("lsblk | grep {}".format(drive_name))
   print (drive_list[1])
   p_size=input("enter size for creating partion")
   type_p=input("enter whether you want to create extended(e) or logical(p)?(p/e): ")
   n_part=s.getstatusoutput("lsblk | grep {} | egrep '{}1|{}2|{}3|{}4' | wc -l".format(drive_name,drive_name,drive_name,drive_name,drive_name,drive_name))
   if (int)(n_part[1])==4:
      print("drive can't create more than 4 partitions!!!")
      print("do you want to delete previous partition?(y/n)")
      ip=input()
      if ip=='y':
        del_p()
        part_3=s.getstatusoutput("lsblk | grep {} | egrep '{}1|{}2|{}3' | wc -l".format(drive_name,drive_name,drive_name,drive_name,drive_name,drive_name))
        if (int)(part_3[1])==3:
            d_part=s.getstatusoutput("echo -e 'p\nn\n{}\n\n+{}\nw\n' |fdisk /dev/{}".format(type_p,p_size,drive_name))
            if d_part[0]==0:
              partprobe=s.getstatusoutput("partprobe /dev/{}".format(drive_name))
              print("partition created successfully!!!")
            else:
              print("error in creating partition or there is alearedy 4 partions created!!!")
        else:
         d_part=s.getstatusoutput("echo -e 'p\nn\n{}\n\n\n+{}\nw\n' |fdisk /dev/{}".format(type_p,p_size,drive_name))
   #print(d_part)
         if d_part[0]==0:
          partprobe=s.getstatusoutput("partprobe /dev/{}".format(drive_name))
          print("partition created successfully!!!")
         else:
          print("error in creating partition or there is alearedy 4 partions created!!!")

        
      else:
        exit()
   else:
    d_part=s.getstatusoutput("echo -e 'p\nn\n{}\n\n\n+{}\nw\n' |fdisk /dev/{}".format(type_p,p_size,drive_name))
   #print(d_part)
    if d_part[0]==0:
      partprobe=s.getstatusoutput("partprobe /dev/{}".format(drive_name))
      print("partition created successfully!!!")
    else:
      print("error in creating partition or there is alearedy 4 partions created!!!")



