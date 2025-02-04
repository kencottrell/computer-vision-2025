
import requests
import time
import importlib

import jmespath
import json
print(jmespath.__path__)

module = importlib.import_module('phyphox-server-phone')  # ken's iphone ip

single_pass = False

# Replace with your device's IP and port
# PHY_ADDRESS = "http://192.168.1.100:8080"
PHY_ADDRESS = module.phone_ip

'''
Basic syntax
   /get?gps_lat&gps_lon&gps_alt&gps_speed&gps_z&gps_accuracy&gps_satellites


Available GPS buffers:
gps_lat: Latitude
gps_lon: Longitude
gps_alt: Altitude
gps_speed: Speed
gps_z: Vertical speed
gps_accuracy: Accuracy of the location
gps_satellites: Number of satellites used

example:
  /get?gps_lat=full&gps_lon=full&gps_alt=full

threshold:
  /get?gps_lat=<last_known_time>&gps_lon=<last_known_time>|gps_lat


  

'''

def query_data(data):
    query = "buffer.{time: time, accX: accX[?@ > `0.015`]}"
    result = jmespath.search(query, data)
    print(result)
    # output    {'time': [0.0, 0.1, 0.2], 'accX': [0.02, 0.03]}


def filter_data(data):
    # To extract only the time and accX data:
    filtered_data = {key: data["buffer"][key] for key in ["time", "accX"]}
    print(filtered_data)
    ''' Output:  {'time': [0.0, 0.1, 0.2], 'accX': [0.01, 0.02, 0.03]}
    Filtering Based on Conditions, If you want to filter accX values greater than 0.015:
    '''
    filtered_accX = [value for value in data["buffer"]["accX"] if value > 0.015]
    print(filtered_accX)
    '''
    Output:  [0.02, 0.03]
    '''



def send_command(command):
    try:
        print("Command to be sent: " + command) 
        response = requests.get(f"{PHY_ADDRESS}/control?cmd={command}")
        if response.status_code == 200:
            print(response.json())  # {"result": true} if successful
        else:
            print(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Failed to send command: {e}")


def start_experiment():
    try:
        response = requests.get(f"{PHY_ADDRESS}/control?cmd=start")
        if response.status_code == 200:
            print("Experiment started:", response.json())
        else:
            print("Failed to start experiment:", response.status_code)
    except Exception as e:
        print(f"Error: {e}")

def stop_experiment():
    response = requests.get(f"{PHY_ADDRESS}/control?cmd=stop")
    if response.status_code == 200:
        print("Experiment stopped:", response.json())
    else:
        print("Failed to Stop experiment:", response.status_code)
    print(response.json())


def fetch_data():
    try:
        # Send a GET request to the /get endpoint
       # response = requests.get(f"{PHY_ADDRESS}/get?buffer&time")
        response = requests.get(f"{PHY_ADDRESS}/get?gps_lat=full&gps_lon=full&gps_alt=full")

        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        json_string = json.dumps(data)
        print("Json dumps: " + json_string)
        # Extract buffer (measured data) and status
        buffer_data = data.get("buffer", {})
       # filtered_data = {key: data["buffer"][key] for key in ["time", "accX"]}
       # print("Filtered data: " + filtered_data)
        status = data.get("status", {})
        
        print("Buffer Data:", buffer_data)
        print("Status:", status)
    except Exception as e:
        print(f"Error fetching data: {e}")

# Example usage
'''
start_experiment()
time.sleep(10)  # Let the experiment run for 5 seconds
fetch_data()
stop_experiment()
'''

if single_pass:    # start experiment, allow remote access and wait for code to start it
    send_command("start")  # Start the experiment
    time.sleep(10)
    fetch_data()
    send_command("stop")   # Stop the experiment
    send_command("clear")
else :    # start experiment and leave running
    fetch_data()