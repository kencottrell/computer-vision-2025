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

from flask import Flask, request

app = Flask(__name__)

@app.route('/sensor-data', methods=['POST'])
def receive_data():
    data = request.json  # Parse JSON data sent by Phyphox
    print(data)          # Log or process the data
    return "Data received", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
