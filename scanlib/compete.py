import requests 
import json 
from colorama import *
import socket

udata = [
        "https://www.chess.com/member/{}", # 1
        "https://dribbble.com/{}",# 2
        "https://{}.carbonmade.com/",# 3
        "https://www.duolingo.com/profile/{}", # 4
        #"https://{}.tumblr.com/",# 5
        #"https://tieba.baidu.com/f?kw={}",# 6
        #"https://www.pinterest.com/{}",# 7
        #"https://vk.com/{}", # 8
        #"https://www.reddit.com/user/{}", # 9
        #"https://mix.com/{}", # 10
        #"https://{}.skyrock.com/", # 11
        #"https://www.facebook.com/{}", # 12
        #"https://bionluk.com/{}", # 13
        #"https://gitlab.com/{}", # 14
        #"https://www.tiktok.com/@{}", # 15
        #"https://www.quora.com/{}", # 16
        #"https://medium.com/@{}", # 17
        #"https://digg.com/@{}", # 18
        #"https://www.linkedin.com/in/{}", # 19
        #"https://www.deviantart.com/{}", # 20
        #"https://www.twitch.tv/{}" # 21	
]
sdata = [
    "status", # 1 
    "status", # 2
    "status",  # 3
    "status"# 4
    #"status",# 5
    #"status",# 6
    #"status",# 7
    #"status",# 8
    #"https://www.reddit.com/user/admwkdamwkdamwkawd",# 9
    #"https://mix.com/", # 10
    #"status",# 11
    #"status",# 12
    #"status", # 13
    #"https://gitlab.com/users/sign_in", # 14
    #"status", # 15
    #"status", # 16
    #"status", # 17
    #"status", # 18
    #"status", # 19
    #"status", # 20
    #"status" # 21
]


def scan(username):
    print(Fore.BLUE+f"""
    
    Competitive & Portfolio & Education Websites Scan : 

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
