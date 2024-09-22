# py -m pip install requests  -- this is the only command that works!!
import requests
import json
import time
import datetime
ct = datetime.datetime.now()
ts = ct.timestamp()

# URL to Xano test API endpoing. Public

url = "https://x8ki-letl-twmt.n7.xano.io/api:8GpeBcyt/event"


data = {
        "camera_timestamp": ts,
        "hotel_id": 59,
        "camera_id": 59,
        "location_id": 12
    }

data_json = json.dumps(data)
headers = {'Content-type': 'application/json'}

response = requests.post(url, data=data_json, headers=headers)
print(data_json)
print(response)