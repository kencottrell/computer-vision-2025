# from the geeks for geeks 
# open cv tutorial https://www.geeksforgeeks.org/extract-images-from-video-in-python/

# py -m pip install opencv-python   -- this is the only command that works!! have to use "py" 
#   not pythong 

import sys
import importlib
import cv2
import os
sys.path.append('inputs')
module = importlib.import_module('video-inout-settings')


print(os.path)
print(cv2.__version__)


# Read the video from specified path 
# cam = cv2.VideoCapture("C:\\Users\\Admin\\PycharmProjects\\project_1\\openCV.mp4") 
inputdir =  module.inputdir
outputdir = module.outputdir
inputname = module.inputname
mp4samplefile = inputdir + inputname + '.mp4'

cam = cv2.VideoCapture(mp4samplefile)
try: 
      
    # creating a folder named data 
    if not os.path.exists(outputdir): 
        os.makedirs(outputdir) 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0
i = 0  
print('reading sample file: ' + mp4samplefile)

while(i < 5): 
    i=i+1  
    # reading from frame 
    ret,frame = cam.read() 
  
    if ret: 
        # if video is still left continue creating images 
        name = outputdir + inputname + '-' + str(currentframe) + '.jpg'
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
