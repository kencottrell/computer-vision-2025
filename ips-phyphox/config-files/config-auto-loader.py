import requests

phyphox_ip = "10.0.0.236"  # Replace with your device's IP
config_url = "http://your-server.com/experiment.phyphox"  # Replace with your file URL

response = requests.get(f"http://{phyphox_ip}:8080/control?cmd=load&url={config_url}")
print(response.status_code, response.text)
