# powershell, for python CLI:  PS C:\Users\kjcot> pip install ultralytics
# for vscode: # py -m pip install ultralytics
import cv2
import numpy as np
from ultralytics import YOLO

import importlib
#import time
import datetime
ct = datetime.datetime.now()

debug = False
module = importlib.import_module('aira-events-tbd')

print('numpy version: ' + np.__version__)
print('YOLO name: ' + YOLO.__name__)

# Load the YOLOv8 model

model = YOLO("yolov8n.pt")  # You can replace this with a different YOLOv8 model
print('model name : ' + model.model_name)
 

# Replace with your IP camera URL

# ip_camera_url = "rtsp://username:password@ip_address:port/stream_path"
# use mp4 without camera

# Read the video from specified path 
# cam = cv2.VideoCapture("C:\\Users\\Admin\\PycharmProjects\\project_1\\openCV.mp4") 

module = importlib.import_module('video-input-settings')

inputdir =  module.inputdir
outputdir = module.outputdir
inputname = module.inputname
ip_camera_url = module.ip_camera_url


 
# cam = cv2.VideoCapture(mp4samplefile)

# Open the IP camera stream

cap = cv2.VideoCapture(ip_camera_url)

 
i = 0
while i < 5:

    ret, frame = cap.read()

    if not ret:

        break

    i = i + 1

    # Perform object detection

    results = model(frame)

 

    # Draw bounding boxes and labels on the frame

    for result in results:
        j = 0
        boxes = result.boxes
        for box in boxes:
            k = 0
            
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            class_id = box.cls[0].item()

            conf = box.conf[0].item()

            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

            cv2.putText(frame, f"{model.names[class_id]} {conf:.2f}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            print("result / box index: " + str(j) + "/" + str(k))
            name = outputdir + inputname +  '-fr' + str(i) +  '.jpg'
            print ('Creating...' + name) 
            cv2.imwrite(name, frame)
            k = k+1
        j = j + 1
    # Display the frame

    cv2.imshow("IP Camera Object Detection", frame)
     # writing the extracted images 
   # cv2.imwrite(name, frame) 
    

 

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

 

cap.release()

cv2.destroyAllWindows()

 

 