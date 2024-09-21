# py -m pip install requests  -- this is the only command that works!!
import requests
import json

url = "https://x8ki-letl-twmt.n7.xano.io/api:8GpeBcyt/event"


data = {
        "created_at": "2024-09-03T14:29:34.000Z",
        "hotels_id": 59,
        "person_id": 59,
        "geo_point": 0.0
    }

data_json = json.dumps(data)
headers = {'Content-type': 'application/json'}

response = requests.post(url, data=data_json, headers=headers)
print(response)