"""
Key Features of the Phyphox API
Control Commands: Use /control to start, stop, or clear experiments:
/control?cmd=start: Starts the experiment.
/control?cmd=stop: Stops the experiment.
/control?cmd=clear: Clears buffers and stops the experiment if running1.
Retrieve Data: Use /get to fetch real-time data in JSON format, which includes sensor readings and experiment status1.

Commands Available via /control
Start the Experiment
    /control?cmd=start
Starts the experiment or the countdown if a timed run is enabled.
Stop the Experiment
    /control?cmd=stop
Stops the currently running experiment.
Clear Buffers
    /control?cmd=clear
Clears all data buffers and stops the experiment if it is running.
Set Buffer Values
    /control?cmd=set&buffer=abc&value=42
Writes a value (e.g., 42) into a specific buffer (e.g., abc). This is typically used for input fields in custom experiments12.

"""

import requests
import time
import importlib

module = importlib.import_module('phyphox-server-phone')  # ken's iphone ip

# Replace with your device's IP and port
# PHY_ADDRESS = "http://192.168.1.100:8080"
PHY_ADDRESS = module.phone_ip



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
        response = requests.get(f"{PHY_ADDRESS}/get")
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        
        # Extract buffer (measured data) and status
        buffer_data = data.get("buffer", {})
        status = data.get("status", {})
        
        print("Buffer Data:", buffer_data)
        print("Status:", status)
    except Exception as e:
        print(f"Error fetching data: {e}")

# Example usage
start_experiment()
time.sleep(10)  # Let the experiment run for 5 seconds
fetch_data()
stop_experiment()
