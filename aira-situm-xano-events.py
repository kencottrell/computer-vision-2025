# py -m pip install requests  -- this is the only command that works!!
import requests
import json
import time
import datetime
ct = datetime.datetime.now()

situmkey = 'e0c828ad924a10e7450d894d3a304db7d6dafa916f26c49c6cba698be80fc7b3'
ts = ct.timestamp()
timenow = ct.strftime("%H:%M:%S")

# URL to Xano test API endpoing. Public

url = "https://x8ki-letl-twmt.n7.xano.io/api:8GpeBcyt/event"


data = {
        "camera_timestamp": timenow,
        "hotel_id": 100,
        "camera_id": 9,
        "location_id": 125
    }

data_json = json.dumps(data)
headers = {'Content-type': 'application/json'}

response = requests.post(url, data=data_json, headers=headers)
print(data_json)
print(response)