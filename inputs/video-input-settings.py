
#import time
import datetime
ct = datetime.datetime.now()

debug = False

inputdir =  "C:\\Users\\kjcot\\mp4files\\"
outputdir = inputdir + "data\\"

inputname = 'guest-checkin'

# set url to 0 for webcam, otherwise mp4 file name
ip_camera_url = inputdir + inputname + '.mp4'

ip_camera_url = 0
inputname = 'kens-webcam'
