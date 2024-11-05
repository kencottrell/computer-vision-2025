# powershell, for python CLI:  PS C:\Users\kjcot> pip install ultralytics
# for vscode: # py -m pip install numpy opencv-python
import cv2 as cv
import numpy as np

print('numpy version: ' + np.__version__)
print('cv  version: ' + cv.__version__)



# Replace with your IP camera URL

# ip_camera_url = "rtsp://username:password@ip_address:port/stream_path"
# here we use mp4 without camera

# Read the video from specified path 
# cam = cv2.VideoCapture("C:\\Users\\Admin\\PycharmProjects\\project_1\\openCV.mp4") 
inputdir =  "C:\\Users\\kjcot\\mp4files\\"
outputdir = inputdir + "\\data\\"
inputname = 'guest-checkin'
ip_camera_url = inputdir + inputname + '.mp4'
 



cap = cv.VideoCapture(ip_camera_url)

 
ret, frame = cap.read()
bbox = cv.selectROI('select', frame, False)

x, y, w, h = bbox

roi = frame[y:y+h, x:x+w]
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_roi, np.array((0., 60., 32.)),
                  np.array((180., 255., 255.)))
roi_hist = cv.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv.normalize(roi_hist, roi_hist, 0, 255, cv.NORM_MINMAX)

term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
i = 0
while(i < 5):
    ret, frame = cap.read()

    if ret:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        ret, track_window = cv.meanShift(dst, bbox, term_crit)

        x, y, w, h = track_window
        img2 = cv.rectangle(frame, (x, y), (x+w, y+h), 255, 2)
        cv.imshow('gfg', img2)

        k = cv.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break
    
    i = i + 1

cap.release()
cv.destroyAllWindows()