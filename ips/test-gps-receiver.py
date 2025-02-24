import requests

# Define the URL of your Flask receiver
url = 'http://192.168.1.206:5000/sensor-data'   # ken's laptop port if necessary

# Define the data to send (if required)
data = {
    'key': 'value',
    'message': 'Test webhook'
}

# Send a POST request to the Flask receiver
response = requests.post(url, json=data)

# Check the response
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
