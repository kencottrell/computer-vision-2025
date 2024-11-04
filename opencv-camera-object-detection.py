# powershell, for python CLI:  PS C:\Users\kjcot> pip install ultralytics
# for vscode: # py -m pip install ultralytics
import cv2
import numpy as np
from ultralytics import YOLO

print('numpy version: ' + np.__version__)
print('YOLO name: ' + YOLO.__name__)

# Load the YOLOv8 model

model = YOLO("yolov8n.pt")  # You can replace this with a different YOLOv8 model
print('model name : ' + model.model_name)
 

# Replace with your IP camera URL

ip_camera_url = "rtsp://username:password@ip_address:port/stream_path"

 

# Open the IP camera stream

cap = cv2.VideoCapture(ip_camera_url)

 

while True:

    ret, frame = cap.read()

    if not ret:

        break

 

    # Perform object detection

    results = model(frame)

 

    # Draw bounding boxes and labels on the frame

    for result in results:

        boxes = result.boxes

        for box in boxes:

            x1, y1, x2, y2 = box.xyxy[0].tolist()

            class_id = box.cls[0].item()

            conf = box.conf[0].item()

 

            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

            cv2.putText(frame, f"{model.names[class_id]} {conf:.2f}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

 

    # Display the frame

    cv2.imshow("IP Camera Object Detection", frame)

 

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

 

cap.release()

cv2.destroyAllWindows()

 

 