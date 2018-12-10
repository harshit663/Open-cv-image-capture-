#!/usr/bin/python36 

import subprocess
import time

samplefile = '/root/Desktop/hello.txt'

def check_java():
    print("Cheching the correct version of Java... ")
    java_ver_out = subprocess.getstatusoutput('java -version')
    if 'Java HotSpot(TM)' in java_ver_out[1]:
        print("You have the correct version  of Java")
        return 0
    else:
        print("You don't have correct version of Java")
        return 1

def install_java():
    bashfile = '/root/.bashrc'
    java_ver = check_java()
    if java_ver == 1:
        print('Installing Java PLEASE WAIT... ')
        java_ooutput = subprocess.getstatusoutput('rpm -ivf jdk-8u171-linux-x64.rpm')
        if java_ooutput[0] == 0:
            subprocess.getoutput('echo "export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/" >> {}'.format(bashfile))
            subprocess.getoutput('echo "export PATH=/usr/java/jdk1.8.0_171-amd64/bin/:$PATH" >> {}'.format(bashfile))
            print("Java sucessfully Installed")
        else:
            print("Error in installing Java")
            print(java_ooutput[1])

def check_hadoop():
    print("Checking the version of Hadoop")
    hadoop_ver_out = subprocess.getstatusoutput('hadoop version')
    if 'Hadoop 1.2.1' in hadoop_ver_out[1]:
        print("You have the correct version of Hadoop")
        return 0
    else:
        print("You don't have correct version of Hadoop")
        return 1        

def install_hadoop():
    had_ver = check_hadoop()
    if had_ver != 0:
        print('Installing Hadoop PLEASE WAIT... ')
        hadoop_out = subprocess.getstatusoutput('rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force')
        if hadoop_out[0] == 0:
            print("Hadoop sucessfully Installed")
        else:
            print("Error in installing Hadoop")
            print(hadoop_out[1])
	

def setup_hadoop():
    hdfs_dir = "/root/Desktop/hdfs-site.xml"
    core_dir = "/root/Desktop/core-site.xml"
    choice = input("Do you want to want to make this computer master? y/n : ")
    if choice == 'y':
        subprocess.getoutput("mkdir /master_disk")
        str_hdfs  = '''
<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>dfs.name</name>
<value>/data</value>
</property>

</configuration>
'''
	
        str_core = '''
<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>fs.default.name</name>
<value>hdfs://192.168.43.3:9001</value>
</property>

</configuration>
'''
        x = subprocess.getstatusoutput('echo "{}" > {}'.format(str_hdfs, hdfs_dir))
        if x[0] == 0:
            print("HDFS XML setup complete")
        else:
            print("Error in HDFS XML setup")
        y = subprocess.getstatusoutput('echo "{}" > {}'.format(str_core, core_dir))
        if y[0] == 0:
            print("CORE XML setup complete")
        else:
            print("Error in CORE XML setup")
    
    elif choice == 'n':
        subprocess.getoutput("mkdir /slave_share")
        str_hdfs  = '''
<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>dfs.data</name>
<value>/share</value>
</property>

</configuration>
'''
	
        str_core = '''
<?xml version=\"1.0\"?>
<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>

<property>
<name>fs.default.name</name>
<value>hdfs://192.168.43.3:9001</value>
</property>

</configuration>
'''
        x = subprocess.getstatusoutput('echo "{}" > {}'.format(str_hdfs, hdfs_dir))
        if x[0] == 0:
            print("HDFS XML setup complete")
        else:
            print("Error in HDFS XML setup")
        y = subprocess.getstatusoutput('echo "{}" > {}'.format(str_core, core_dir))
        if y[0] == 0:
            print("CORE XML setup complete")
        else:
            print("Error in CORE XML setup")
    
    '''filehdfs = open(set_hdfs, 'w')
    filehdfs.write(str_hdfs)
    filehdfs.close()
        
    filecore = open(set_core, 'w')
    filecore.write(str_core)
    filecore.close()'''
     
        
def setup_master():
    print("Checking...")
    hadoop_check_out = subprocess.getstatusoutput('echo Y | hadoop namenode -format')
    if hadoop_check_out[0] == 0:
        print("No Error in HDFS and CORE XML")
    else:
        print("Error...")
    print(subprocess.getoutput('iptables -F'))
    print(subprocess.getoutput('hadoop-daemon.sh start namenode'))
    namenode_check = subprocess.getstatusoutput('jps')
    if namenode_check[0] == 0:
        print("Hadoop configured correctly")
        print(namenode_check[1])
    else:
        print("Hadoop not configured correctly")
        print(namenode_check[1])
        
def check_connection():
    print("Checking Connection PLEASE WAIT...")
    time.sleep(5)
    hadoop_status = subprocess.getstatusoutput('hadoop dfsadmin -report')
    if hadoop_status[0] == 0:
        print("Connection sucessful")
        print(hadoop_status[1])
    else:
        print("Connection Failed...")
        
    
def setup_slave():
    subprocess.getoutput('iptables -F')
    out = subprocess.getstatusoutput('hadoop-daemon.sh start datanode')
    if out[0] == 0:
        print("Service started sucessfully")
    else:
        print("Service could not start")
    datanode_check = subprocess.getstatusoutput('jps')
    if datanode_check[0] == 0:
        print("Hadoop configured correctly")
        print(datanode_check[1])
    else:
        print("Hadoop not configured correctly")
        print(datanode_check[1])



        
if __name__ == '__main__':
    print("Welcome To Hadoop Setup")
    install_java()
    install_hadoop()
    check_hadoop()
    #setup_hadoop()
    #setup_slave()
    #setup_master()
    #check_connection()



