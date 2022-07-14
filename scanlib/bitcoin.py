import requests 
import json 
from colorama import *
import socket

udata = [
        "https://www.minds.com/{}", # 1
        "https://bitcoinforum.com/profile/{}/",# 2
        "https://www.analystforum.com/u/{}",# 3
        "http://www.money-talk.org/profile.php?mode=viewprofile&u={}" # 4
]
sdata = [
    "status", # 1 
    "https://bitcoinforum.com/profile/adminofwebsite/", # 2
    "status",# 3
    "http://www.money-talk.org/profile.php?mode=viewprofile&u=dawd"# 4
]


def scan(username):
    print(Fore.BLUE+f"""
    
    Bitcoin & Financial Websites Scan : 

    """)
    asia = 0
    western = 0
    for i in range(0,len(udata)):
        if sdata[i] == "status":
            url = udata[i].format(username)
            r = requests.get(url)
            if r.status_code == 200 : 
                print(Fore.GREEN+f"[+] User Found : {url}")
            else:
                print(Fore.RED+f"[-] Not Found  : {url}")
        else:
            url = udata[i].format(username)
            r1 = requests.get(url).text
            r2 = requests.get(sdata[i]).text
            if r1 == r2:
                print(Fore.GREEN+f"[+] User Found  : {url}")
            else:
                print(Fore.RED+f"[-] Not Found  : {url}")
