# use "py" - - pip install flask opencv-python
# py -m pip install <package>   -- this is the only command that works!!


'''
Flask Integration: Use Flask to serve the RTSP stream. 
You can use OpenCV to capture frames from the RTSP stream and serve them using Flask.
OpenCV and Flask: Capture the RTSP stream with OpenCV and serve it via Flask:
'''

from flask import Flask, Response
import cv2

app = Flask(__name__)

def generate_frames():
    cap = cv2.VideoCapture("rtsp://localhost:8554/test")
    while True:
        success, frame = cap.read()
        if not success:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)