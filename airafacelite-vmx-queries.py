# py -m pip install requests  -- this is the only command that works!!
import importlib
import requests

import json
#import time
import datetime
import pprint
ct = datetime.datetime.now()
timenow = ct.strftime("%H:%M:%S")
aira_token  = '643d6a3d253d5e7b7276713d333d6f3d253d2e2d2c2b2a293d333d6b3d252e282d282b2a26272628272a28333d673d253d5e7b7276713d62'
ts = ct.timestamp()
timenow = ct.strftime("%H:%M:%S")

true = True  # expected payload for AiraFace below
false = False # expected spelling for AiraFace below 

aira_create_event_payload = {
  "action_type": "http",
  "name": "Kens_Test_Event",
  "enable": true,
  "group_list": [
    "All Person"
  ],
  "divice_groups":[
    "cdc97c86-5f06-4504-914e-87172af202c5"
  ],
  "temperature_trigger_rule": 0,
  "remarks": "This is a test from Kens VSCode python program",
  "specify_time": {
    "list": [
      {
        "start_time": 1704556800000,
        "end_time": 1705075200000
      }
    ]
  },
  "weekly_schedule": {
    "list": [
      {
        "day_of_week": 2,
        "hours_list": [8, 9]
      }
    ]
  },
  "https": true, "method": "GET", "user": "username", "pass": "password",  "host": "192.168.2.3", "port": 80, "data_type": "JSON",  "language": "en",
  "url": "/?aaa=##VerifiedTimeStamp##&bbb=##IsStranger##&", "custom_data": "", "note" : ""
 }

aira_create_event_json = json.dumps(aira_event_payload)

module = importlib.import_module('aira-events-tbd')
 


# URL to local VMX image in this laptop

airaface_url_create_ev_handle = 'https://192.168.1.241:443/airafacelite/createeventhandle'

airaface_url_get_ev_handles = 'https://192.168.1.241:443/airafacelite/findeventhandle'

headers = {'Content-type': 'application/json', 
                     'token' : aira_token }

response1 = requests.get(airaface_url_get_ev_handles, headers=headers)

response2 = requests.get(airaface_url_get_ev_handles, headers=headers)
 


print('Aira Event  Handle Create ===================')
pprint.pprint (response1.text, indent=4)
print('Aira Event  Handle List  ===================')
pprint.pprint (response2.text, indent=4)
#payload = json.dumps(response.text)
#print(payload)