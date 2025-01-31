import requests

# Replace with your Phyphox device's IP and port
PHY_ADDRESS = "http://192.168.x.x:8080"

def start_experiment():
    try:
        response = requests.get(f"{PHY_ADDRESS}/control?cmd=start")
        if response.status_code == 200:
            print("Experiment started:", response.json())
        else:
            print("Failed to start experiment:", response.status_code)
    except Exception as e:
        print(f"Error: {e}")

start_experiment()
