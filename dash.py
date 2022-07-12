from colorama import *
import optparse
import datetime
from scanlib import socialmedia
import requests
import socket 
import os
def banner():
    print(Fore.BLACK+f"""
     _____  _______ _______ _______ 
    |     \|   _   |     __|   |   |
    |  --  |       |__     |       |
    |_____/|___|___|_______|___|___| 1.6

                        [!] This OSINT Tool created and developed by TheSadError
    """)

def start(username,time):
    os.system('cls' if os.name=='nt' else 'clear')
    banner()    
    print(Fore.RED+f"""
    Contact :

    Github  : https://github.com/TheSadError
    Youtube : https://www.youtube.com/channel/UCUfTuo3-85qD_7v1n-W98rw
    Discord : err0r#4018
    """)
    print(Fore.BLUE+f"\nStarting DASH OSINT scanner... ( https://github.com/TheSadError/DASH ) Time : {time}")
    socialmedia.scan(username)

def main():
    time= datetime.datetime.now()
    parser = optparse.OptionParser(f" sudo python3 dash.py --u username")

    parser.add_option("-u","--u",dest = "username",type="string") # username parameter
    (options,args) = parser.parse_args()
    username = options.username
    if(username == None ):
        banner()
        print(parser.usage)
        exit(0)
    start(username,time)


if __name__ == "__main__":
    main()
