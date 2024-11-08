
​
import cv2
import subprocess as sp

def gstreamer_pipeline_out():
    return (
        "appsrc ! "
        "video/x-raw, format=BGR ! "
        "videoconvert ! "
        "x264enc tune=zerolatency bitrate=500 speed-preset=superfast ! "
        "rtph264pay config-interval=1 pt=96 ! "
        "udpsink host=127.0.0.1 port=8554"
    )

video_path = "demo.mp4"
capture = cv2.VideoCapture(video_path)

out = cv2.VideoWriter(gstreamer_pipeline_out(), cv2.CAP_GSTREAMER, 0, 30, (640, 480))

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break
    out.write(frame)

capture.release()
out.release()


Get Outlook for iOS