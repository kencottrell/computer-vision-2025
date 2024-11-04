# from the geeks for geeks 
# open cv tutorial https://www.geeksforgeeks.org/extract-images-from-video-in-python/

# py -m pip install opencv-python   -- this is the only command that works!! have to use "py" 
#   not pythong 

import cv2
import os
print(os.path)
print(cv2.__version__)

# Read the video from specified path 
# cam = cv2.VideoCapture("C:\\Users\\Admin\\PycharmProjects\\project_1\\openCV.mp4") 
mp4samplefile = "C:\\Users\\kjcot\\mp4files\\aira-sample.mp4"
cam = cv2.VideoCapture(mp4samplefile)
print('reading sample file: ' + mp4samplefile)
try: 
      
    # creating a folder named data 
    if not os.path.exists("C:\\Users\\kjcot\\mp4files\\data"): 
        os.makedirs("C:\\Users\\kjcot\\mp4files\\data") 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0
i = 0  
while(i < 5): 
    i=i+1  
    # reading from frame 
    ret,frame = cam.read() 
  
    if ret: 
        # if video is still left continue creating images 
        name = "C:\\Users\\kjcot\\mp4files\\data\\" + str(currentframe) + '.jpg'
        print ('Creating...' + name) 
  
        # writing the extracted images 
        cv2.imwrite(name, frame) 
  
        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += 1
    else: 
        break
  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 
