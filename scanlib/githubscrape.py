import json
from re import I
import requests
from colorama import *
import scanlib.js as js
def getinfo(username):
    url = "https://api.github.com/users/{}".format(username)
    data = requests.get("https://api.github.com/users/{}".format(username)).text
    js.jsd("error", data)
    need = [
            'name',
            'type',
            'company',
            'location',
            'email'
        ]
    req = requests.get(url).json()
    dt = js.pdata(need, req)
    print(json.dumps(dt, indent= True))
