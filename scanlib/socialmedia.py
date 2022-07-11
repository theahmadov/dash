import requests 
import json 
from colorama import *

udata = [
        "https://github.com/",
        "https://instagram.com/"
]
sdata = [
    "status",
    "https://instagram.com/"
]

def scan(username):
    print(Fore.BLACK+f"""
    
    Social Media Scan : 

    """)
    for i in range(0,len(udata)):
        if sdata[i] == "status":
            url = udata[i]+username
            r = requests.get(url)
            if r.status_code == 200 : 
                print(Fore.GREEN+f"SUCCESS! User found  : {url}")
            else:
                print(Fore.RED+f"FAILED! User not found : {url}")
        else:
            url = udata[i]+username
            r1 = requests.get(url).text
            r2 = requests.get(sdata[i]).text
            if r1 == r2:
                print(Fore.RED+f"FAILED! User not found : {url}")
            else:
                print(Fore.GREEN+f"SUCCESS! User found  : {url}")