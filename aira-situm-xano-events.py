# py -m pip install requests  -- this is the only command that works!!
import requests
import json
#import time
import datetime
import pprint
ct = datetime.datetime.now()

import importlib
module = importlib.import_module('aira-events-tbd')
print(module.testPayload)
print("===========================")
situmkey = 'e0c828ad924a10e7450d894d3a304db7d6dafa916f26c49c6cba698be80fc7b3'
ts = ct.timestamp()
timenow = ct.strftime("%H:%M:%S")

# URL to Xano test API endpoing. Public

xanourl = "https://x8ki-letl-twmt.n7.xano.io/api:8GpeBcyt/event"
situm_url = 'https://dashboard.situm.com/api/v1/buildings'

xanodata = {
        "camera_timestamp": timenow,
        "hotel_id": 100,
        "camera_id": 9,
        "location_id": 125
    }

data_json = json.dumps(xanodata)
headers = {'Content-type': 'application/json'}

response = requests.post(xanourl, data=data_json, headers=headers)
print(data_json)
print('Xano: ' + str(response))

headers = {'Content-type': 'application/json', 
                     'X-API-KEY' :'e0c828ad924a10e7450d894d3a304db7d6dafa916f26c49c6cba698be80fc7b3' }
response = requests.get(situm_url, headers=headers)
print('Situm: ')
print('====================================')
pprint.pprint (response.text)
#payload = json.dumps(response.json, indent=6)
#print(payload)