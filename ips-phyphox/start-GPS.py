
import requests
import time
import importlib
import subprocess
import sys
import jmespath
import json
import os
from urllib3.exceptions import NameResolutionError

print(jmespath.__path__)
print(sys.api_version, os.path, json.__name__)

module = importlib.import_module('settings')  # ken's iphone ip

single_pass = False

# Replace with your device's IP and port
# PHY_ADDRESS = "http://192.168.1.100:8080"
PHY_ADDRESS = module.phone_ip

'''
Basic syntax
   /get?gps_lat&gps_lon&gps_alt&gps_speed&gps_z&gps_accuracy&gps_satellites




example:
  /get?gps_lat=full&gps_lon=full&gps_alt=full

threshold:
  /get?gps_lat=<last_known_time>&gps_lon=<last_known_time>|gps_lat

'''

CONFIG_FILE_SERVICE_RUNNING = False


def load_config_file():

    config_url = module.CONFIG_URL
    # config_url = "http://your-serverC.com/experiment.phyphox"  # Replace with your file URL
    try: 
        response = requests.get(f"http://{PHY_ADDRESS}:8080/control?cmd=load&url={config_url}")
        print(response.status_code, response.text)
    except Exception as e:
        print(f"Failed to load config file: {e}")

def run_config_file_server():    
#  subprocess.run(["python", "./ips-phyphox/config-http-file-server1.py"]) 
# Start the subprocess in the background
    subprocess.Popen(["python", "./ips-phyphox/config-http-file-server1.py"], 
                     creationflags=subprocess.CREATE_NEW_CONSOLE)








def poll_gps_data():
    #CHANNELS = ["latitude", "longitude", "altitude"]  # Example channels for GPS data
    CHANNELS = ["lat", "lon", "z", "t"]  # Example channels for GPS data

    while True:
        try:
        # Build the URL for data retrieval
            url = f"{PHY_ADDRESS}/get?" + "&".join(CHANNELS)
            response = requests.get(url)
            data = response.json()
      

        # Process the received data
            print("-----")
            for channel in CHANNELS:
                values = data["buffer"][channel]["buffer"]
                print(f"{channel}: {values[-1]}")  # Print the most recent value
               

    
        except Exception as e:
            print("Error:", e)
      
    
       

        time.sleep(1)  # Adjust interval as needed
        '''
            for filtering:
            To use the /get command in Phyphox for retrieving GPS data via the remote interface, you can specify the desired buffers in your request. For example:
            Basic Request: /get?latitude&longitude
            This retrieves the latest latitude and longitude values.
            Full Buffer: /get?latitude=full&longitude=full
            This returns the full buffer of recorded latitude and longitude values.
            Threshold-Based: /get?latitude=42&longitude=42|time
            This fetches latitude and longitude values starting from the timestamp where the "time" buffer exceeds 42.
            Make sure to encode special characters like | as %7C in the URL if needed
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



run_config_file_server()
load_config_file()
poll_gps_data()
