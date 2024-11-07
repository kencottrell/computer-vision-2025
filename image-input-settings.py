
#import time
import datetime
ct = datetime.datetime.now()

debug = False

inputdir =  "C:\\Users\\kjcot\\mp4files\\photos\\"
outputdir = inputdir + "data\\"
inputname = 'norma'

# set url to 0 for webcam, otherwise mp4 file name
ip_camera_url = inputdir + inputname + '.jpg'

ip_camera_url = str(ip_camera_url)   # not sure why this has to be recast