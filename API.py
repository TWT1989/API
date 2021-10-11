# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 01:03:10 2021

@author: Tim
"""

import requests
import json


ID = input('Input GitHub User ID: ')
URL = "https://api.github.com/users/{}/repos".format(ID)

data = {"name" : "id"}

response = requests.get(URL,data=json.dumps(data))
response = json.loads(response.text)


for x in response:
    print('repo name:') 
    x["name"]
    print(x["name"])
    C = "https://api.github.com/repos/{}/{}/commits".format(ID, x["name"])
    output = requests.get(C,data=json.dumps(data))
    output = json.loads(output.text)
    length = len(output)
    print('number of commits:') 
    print(length)
        
        
    