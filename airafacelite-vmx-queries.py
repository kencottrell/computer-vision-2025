# py -m pip install requests  -- this is the only command that works!!
# pip install pip-system-certs
# pip install python-certifi-win32
# these cert installs didn't work so had to use verify=False for calls instead
#  refer to this perplexity.ai article: 
#         https://www.perplexity.ai/search/caused-by-sslerror-sslcertveri-SAkx.H57SAmZiLFKCylb3A 
import importlib
import requests

import json
#import time
import datetime
import pprint
ct = datetime.datetime.now()
timenow = ct.strftime("%H:%M:%S")
ts = ct.timestamp()
timenow = ct.strftime("%H:%M:%S")
module = importlib.import_module('aira-events-tbd')



aira_get_handle_payload = {
    "uuid": "",                                 # optional  default ""
    "action_type": ["http", "line", "mail"]     #  optional  default []
}



# aira_create_event_json = json.dumps(aira_create_event_payload)
aira_get_ev_payload_json = json.dumps(aira_get_handle_payload)

 


# URL to local VMX image in this laptop

airaface_url_get_token = 'https://192.168.1.241:443/airafacelite/generatetoken'
body = {
    "username":"Admin",
    "password":"123456"
}
body_json = json.dumps(body)
headers = {'Content-type': 'application/json' }
response = requests.post(airaface_url_get_token, data=body_json, headers = headers, verify=False)
print(response.text)

token = response.text
airaface_url_create_ev_handle = 'https://192.168.1.241:443/airafacelite/createeventhandle'

airaface_url_get_ev_handles = 'https://192.168.1.241:443/airafacelite/findeventhandle'
aira_token = '643d6a3d253d5e7b7276713d333d6f3d253d2e2d2c2b2a293d333d6b3d252e282d282a29292d2b292f2a28333d673d253d5e7b7276713d62'
headers = {'Content-type': 'application/json', 
    'token': aira_token }
response1 = requests.get(airaface_url_create_ev_handle, headers=headers, verify=False)
print('Aira Event  Handle Create ===================')
pprint.pprint (response1.text, indent=4)

response2 = requests.post(airaface_url_get_ev_handles, data=aira_get_ev_payload_json, headers=headers, verify=False)
print('Aira Event  Handle List  ===================')
pprint.pprint (response2.text, indent=4)
#payload = json.dumps(response.text)
#print(payload)