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

debug = False


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
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Access the specific parameter
    aira_token = data["token"]

    # Print the parameter value
    print("Token value: ")
    print(aira_token)
else:
    # Handle errors
    print("Error:", response.status_code)

airaface_url_create_ev_handle = 'https://192.168.1.241:443/airafacelite/createeventhandle'

airaface_url_get_ev_handles = 'https://192.168.1.241:443/airafacelite/findeventhandle'

headers = {'Content-type': 'application/json', 
    'token': aira_token }
body = module.aira_create_event_payload  
body_json = json.dumps(body)
response1 = requests.get(airaface_url_create_ev_handle, data=body_json, headers=headers, verify=False)



#with open('airaEventCreateHandle.json', 'w', encoding='utf-8') as f:
#    datajson = json.loads(response1.text)
#    json.dump(datajson, f, ensure_ascii=False, indent=4)

response2 = requests.post(airaface_url_get_ev_handles, data=aira_get_ev_payload_json, headers=headers, verify=False)


with open('airaGetEventHandles.json', 'w', encoding='utf-8') as f:
    datajson = json.loads(response2.text)
    json.dump(datajson, f, ensure_ascii=False, indent=4)


if debug:
    print('Aira Event  Handle Create ===================')
    pprint.pprint (response1.text, indent=4)
    print('Aira Event  Handle List  ===================')
    pprint.pprint (response2.text, indent=4)
    #payload = json.dumps(response.text)
    #print(payload)