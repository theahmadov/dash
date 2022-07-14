import requests 
import json 
from colorama import *
import socket

udata = [
        "https://www.chess.com/member/{}", # 1
        "https://dribbble.com/{}",# 2
        "https://{}.carbonmade.com/",# 3
        "https://www.duolingo.com/profile/{}", # 4
        "https://www.artstation.com/{}",# 5
        "https://www.behance.net/{}",# 6
        "https://www.buymeacoffee.com/{}",# 7
        "https://codepen.io/{}", # 8
        "https://www.colourlovers.com/lover/{}", # 9
        "https://lichess.org/@/{}",
        "https://www.lesswrong.com/users/{}",
        "https://{}.newgrounds.com/",
        "https://opensource.com/users/{}",
        "https://pastebin.com/u/{}",
        "https://www.polygon.com/users/{}",
        "https://www.sportlerfrage.net/nutzer/{}",
        "https://unsplash.com/@{}"
]
sdata = [
    "status", # 1 
    "status", # 2
    "status",  # 3
    "status",# 4
    "status",# 5
    "status",# 6
    "status",# 7
    "status",# 8
    "status",# 9
    "status",
    "status",
    "status",
    "status",
    "status",
    "status",
    "status",
    "status"
]


def scan(username):
    print(Fore.BLUE+f"""
    
    Competitive & Portfolio & Education & News Websites Scan : 

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
