# note images need to be larger for this to work...
import cv2
import  importlib
# import os
import sys
sys.path.append('inputs')


module = importlib.import_module('image-input-settings')


inputdir =  module.inputdir
outputdir = module.outputdir
inputname = module.inputname
ip_camera_url = module.ip_camera_url

# Load a pre-trained face detector classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

image = cv2.imread(ip_camera_url)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

# Detect Objects: Use the classifier to detect objects in the image.
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)
#faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

num_faces = len(faces)
print(f"Number of faces detected: {num_faces}")

# Draw Rectangles Around Detected Objects: For each detected object, draw a rectangle around it.
for (x, y, w, h) in faces:
    cv2.rectangle(gray_image, (x, y), (x+w, y+h), (255, 0, 0), 2)
# Display the Result:
cv2.imshow('Detected Faces', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()