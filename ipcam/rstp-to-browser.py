# use "py" - - pip install flask opencv-python
# py -m pip install <package>   -- this is the only command that works!!

## http://localhost:5000/video_feed

'''
Open a browser and go to http://<your_ip>:5000/video_feed to view the video stream.
This setup captures video frames using OpenCV and streams them via Flask, 
effectively turning your application into a virtual IP camera

'''
import sys
import importlib

from flask import Flask, Response
import cv2

sys.path.append('inputs')
module = importlib.import_module('video-inout-settings')

#ip_cameral_url = module.ip_camera_url
ip_cameral_url = module.output_rstp
app = Flask(__name__)

print('reading this producer  to send to browser: ' + ip_cameral_url)
def generate_frames():
    cap = cv2.VideoCapture(ip_cameral_url)  # Use 0 for webcam or replace with IP camera URL
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')