import requests 
import json 
from colorama import *
import socket
udata = [
        "https://github.com/{}", # 1
        "https://instagram.com/{}",# 2
        "https://twitter.com/{}",# 3
        "https://t.me/{}", # 4
        "https://{}.tumblr.com/",# 5
        "https://tieba.baidu.com/f?kw={}",# 6
        "https://www.pinterest.com/{}",# 7
        "https://vk.com/{}", # 8
        "https://www.reddit.com/user/{}", # 9
        "https://mix.com/{}", # 10
        "https://{}.skyrock.com/"
]
sdata = [
    "status", # 1 
    "https://instagram.com/", # 2
    "status",# 3
    "status",# 4
    "status",# 5
    "status",# 6
    "https://www.pinterest.com/ideas/",# 7
    "status",# 8
    "status",# 9
    "https://mix.com/", # 10
    "status"# 11
]

class info:
    country = []
    city = []
    age = 0

def scan(username):
    print(Fore.BLACK+f"""
    
    Social Media Scan : 

    """)
    for i in range(0,len(udata)):
        if sdata[i] == "status":
            url = udata[i].format(username)
            r = requests.get(url)
            if r.status_code == 200 : 
                print(Fore.GREEN+f"[+] User Found : {url}")
            else:
                print(Fore.RED+f"[!] Not Found  : {url}")
        else:
            url = udata[i].format(username)
            r1 = requests.get(url).text
            r2 = requests.get(sdata[i]).text
            if r1 == r2:
                print(Fore.GREEN+f"[+] User Found  : {url}")
            else:
                print(Fore.RED+f"[!] Not Found  : {url}")
