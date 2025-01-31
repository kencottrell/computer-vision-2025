import requests

'''
Explanation
Endpoint: The /get endpoint retrieves both the measured data (buffer) and the experiment's current status (status) in JSON format 1.
Response Structure:
buffer: Contains experimental data (e.g., time, acceleration, etc.).
status: Includes metadata like whether the experiment is running.
Example Output
The output might look like this:
json
{
  "buffer": {
    "time": [0.0, 0.1, 0.2],
    "accX": [0.01, 0.02, 0.03]
  },
  "status": {
    "measuring": true,
    "paused": false
  }
}
This script provides a straightforward way to retrieve real-time sensor data from Phyphox experiments using Python 13.

'''

# Replace with your Phyphox device's IP and port
PHY_ADDRESS = "http://192.168.1.100:8080"

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

# Fetch and display data
fetch_data()
