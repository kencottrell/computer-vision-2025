# py -m pip install requests  -- this is the only command that works!!
import requests
import json
#import time
import datetime
ct = datetime.datetime.now()


ts = ct.timestamp()
timenow = ct.strftime("%H:%M:%S")

# URL to Xano test API endpoing. Public


url ="https://x8ki-letl-twmt.n7.xano.io/api:dptOGfrO/smartwatchalertbuttonevents"


data = {
        "deviceID": timenow,
        "latitude": 59.59,
        "longitude": 89.54,
        "altitude": 12.0
    }

data_json = json.dumps(data)
headers = {'Content-type': 'application/json'}

response = requests.post(url, data=data_json, headers=headers)
print(data_json)
print(response)