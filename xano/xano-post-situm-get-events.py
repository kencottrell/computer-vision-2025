# py -m pip install requests  -- this is the only command that works!!
import importlib
import requests
import json
#import time
import datetime
import pprint
ct = datetime.datetime.now()

debug = False
module = importlib.import_module('aira-events-tbd')
if debug: 
    print(module.testPayload)
    print("===========================")



ts = ct.timestamp()
timenow = ct.strftime("%H:%M:%S")

# URL to Xano test API endpoing. Public

xanourl = "https://x8ki-letl-twmt.n7.xano.io/api:8GpeBcyt/event"


camera_event = {
        "camera_timestamp": timenow,
        "hotel_id": 100,
        "camera_id": 9,
        "location_id": 125
    }

camera_event_json = json.dumps(camera_event)
headers = {'Content-type': 'application/json'}

response = requests.post(xanourl, data=camera_event_json, headers=headers)
print(camera_event_json)
print('Xano: ' + str(response))


headers = {'Content-type': 'application/json', 
                     'X-API-KEY' :'e0c828ad924a10e7450d894d3a304db7d6dafa916f26c49c6cba698be80fc7b3' }

'''
response = requests.get(situm_url, headers=headers)
if debug:
    print('Situm: ====================================')
    pprint.pprint (response.text, indent=4)

with open('allBuildings.json', 'w', encoding='utf-8') as f:
    datajson = json.loads(response.text)
    json.dump(datajson, f, ensure_ascii=False, indent=4)

'''

#payload = json.dumps(response.text)
#print(payload)