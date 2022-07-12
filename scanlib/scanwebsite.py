import requests
from colorama import *
from urllib.request import urlopen
from urllib.error import *

lst = [
    "http://{}.cf",
    "http://{}.tl",
    "http://{}.ml",
    "http://{}.com",
    "http://{}.org",
    "http://{}.me",
    "http://{}.info",
    "http://{}.net",
    "http://{}.online",
    "http://{}.site",
    "http://{}.tr",
    "http://{}.de",
    "http://{}.app",
    "http://{}.live",
    "http://{}.store",
    "http://{}.shop",
    "http://{}.website",
    "http://{}.xyz",
    "http://{}.plus",
    "http://{}.bet",
    "http://{}.group",
    "http://{}.io"
]

def scan(username):
    print(Fore.BLACK+f"""
    
    Website Domain Scan : 

    """)
    for i in range(0, len(lst)):
        url = lst[i].format(username)
        try :
            req = requests.get(url)
            found = True
        except:
            found = False
        if found == True:
            print(Fore.GREEN+f"[+] Website Found    : {url}")
            #print(Fore.RED+f"[!] Website Not Found : {url}")
            
