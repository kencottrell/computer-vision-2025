
import requests
import time
import importlib
import subprocess
import sys
import jmespath
import json
import os
from urllib3.exceptions import NameResolutionError

from flask import Flask, request, jsonify



app = Flask(__name__)

print(app.name, jmespath.__path__, sys.api_version, os.path, json.__name__, jsonify.__class__)


'''
edit .phyphox config file:
 <network>
    <connection interval="1" address="https://yourserver.com/api/input" id="submit" service="http/post" conversion="json" privacy="https://your-privacy-policy-url.com" autoConnect="true">
        <send id="sensorData" type="buffer">bufferName</send>
    </connection>
 </network>

interval: Sets how often (in seconds) data is sent.
address: The URL of your network service.
service: Protocol used (e.g., http/post or mqtt).
send: Specifies the buffer containing sensor data

Define which sensor data to send by assigning it to buffers in your experiment configuration.
Example:
xml
<buffer id="bufferName" type="array"/>

Trigger Data Transmission
Use either:
The interval property for periodic transmission.
A button trigger with <trigger> in your experiment configuration

setup the event /sensor-data endpoint

<network>
    <connection address="http://<server-ip>:5000/sensor-data" service="http/post" conversion="json" interval="1">
        <send id="sensorData" type="buffer">bufferName</send>
    </connection>
</network>

'''


print(jmespath.__path__)
print(sys.api_version, os.path, json.__name__)

module = importlib.import_module('settings')  # ken's iphone ip
# Replace with your device's IP and port
# PHY_ADDRESS = "http://192.168.1.100:8080"
PHY_ADDRESS = module.phone_ip
single_pass = False


CONFIG_FILE_SERVICE_RUNNING = False

'''
curl -X POST -H "Content-Type: application/json" -d '{"key1": "value1", "key2": 123}' http://localhost:5000/sensor-data
'''

def load_config_file():

    config_url = module.CONFIG_URL
    device_url = f"{PHY_ADDRESS}/control?cmd=load&url={config_url}"
    # config_url = "http://your-serverC.com/experiment.phyphox"  # Replace with your file URL
    try: 
        response = requests.get(device_url)
        print(response.status_code, response.text)
    except Exception as e:
        print(f"Failed to load config file: {e}")

def run_config_file_server():    
#  subprocess.run(["python", "./ips-phyphox/config-http-file-server1.py"]) 
# Start the subprocess in the background
    subprocess.Popen(["python", "./ips-phyphox/config-http-file-server1.py"], 
                     creationflags=subprocess.CREATE_NEW_CONSOLE)


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

testconfig = False
if testconfig:
    run_config_file_server()
    load_config_file()

@app.route('/sensor-data', methods=['POST'])
def receive_data():

    if request.is_json:
        data = request.get_json()
            # Process the received JSON data
        print ("mesg received from GPS sensor: " + json.dumps(data))
        return jsonify({"message": "Data received successfully", "data": data}), 200
    else:
        return jsonify({"error": "Invalid Content-Type"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
