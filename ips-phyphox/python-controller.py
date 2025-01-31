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

# Replace with your device's IP and port
PHY_ADDRESS = "http://192.168.1.100:8080"


def start_experiment():
    response = requests.get(f"{PHY_ADDRESS}/control?cmd=start")
    print(response.json())


def stop_experiment():
    response = requests.get(f"{PHY_ADDRESS}/control?cmd=stop")
    print(response.json())


def fetch_data():
    response = requests.get(f"{PHY_ADDRESS}/get")
    data = response.json()
    print(data)


# Example usage
start_experiment()
time.sleep(5)  # Let the experiment run for 5 seconds
fetch_data()
stop_experiment()
