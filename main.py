
from datetime import datetime 
import socket 
import subprocess
import sys 

subprocess.call('clear', shell=True)

print(r""" ███╗░░░███╗██╗██████╗░░█████╗░██╗░░██╗██╗░░░░░███████╗░██████╗░█████╗░
████╗░████║██║██╔══██╗██╔══██╗██║░██╔╝██║░░░░░██╔════╝██╔════╝██╔══██╗
██╔████╔██║██║██████╔╝███████║█████═╝░██║░░░░░█████╗░░╚█████╗░███████║
██║╚██╔╝██║██║██╔══██╗██╔══██║██╔═██╗░██║░░░░░██╔══╝░░░╚═══██╗██╔══██║
██║░╚═╝░██║██║██║░░██║██║░░██║██║░╚██╗███████╗███████╗██████╔╝██║░░██║
╚═╝░░░░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░╚═╝░░╚═╝

░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║""")

print("\n****************************************************************")
print("\n* https://github.com/MiraklesA                                 *")
print("\n****************************************************************")

#Input 
target_ip = input("\nEnter an Ip Address to scan for open Ports (Note this doesn't define what the port type is :'))) : ")
targetdetails = socket.gethostbyname(target_ip)


print ("_"* 60)
print ("\nScanning, this might take some time (Single Threaded Scanning)")
print ("_"* 60)

time = datetime.now()


try: 
    for port in range (1,65535): 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((targetdetails,port))
        if result ==0: 
            print("Port {} is open".format(port))
        sock.close 



except socket.gaierror: 
    print ("\nCouldn't connec to the server")
    sys.exit 

except socket.error:
    print ("\n No response")
    sys.exit() 

except KeyboardInterrupt: 
    print ("\n Exiting no data will be saved")
    sys.exit()

time2 = datetime.now() 
total = time2 - time

print ('Full Scan has been completed in:', total) 


