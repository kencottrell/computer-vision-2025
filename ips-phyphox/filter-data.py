# pip install jmespath
import jmespath
print(jmespath.__path__)
data = {
    "buffer": {
        "time": [0.0, 0.1, 0.2],
        "accX": [0.01, 0.02, 0.03],
        "accY": [0.04, 0.05, 0.06]
    },
    "status": {
        "measuring": True,
        "paused": False
    }
}


# To extract only the time and accX data:

filtered_data = {key: data["buffer"][key] for key in ["time", "accX"]}
print(filtered_data)
'''

Output: 
    {'time': [0.0, 0.1, 0.2], 'accX': [0.01, 0.02, 0.03]}
Filtering Based on Conditions, If you want to filter accX values greater than 0.015:
'''

filtered_accX = [value for value in data["buffer"]["accX"] if value > 0.015]
print(filtered_accX)
'''
Output:
    [0.02, 0.03]


'''



query = "buffer.{time: time, accX: accX[?@ > `0.015`]}"
result = jmespath.search(query, data)
print(result)

# output    {'time': [0.0, 0.1, 0.2], 'accX': [0.02, 0.03]}
