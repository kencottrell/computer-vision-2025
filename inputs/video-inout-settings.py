
#import time
import datetime
import socket

ct = datetime.datetime.now()

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

localhost = get_ip()
print(get_ip())

debug = False

inputdir =  "C:\\Users\\kjcot\\mp4files\\"
outputdir = inputdir + "data\\"
output_rstp = 'rtsp://' + localhost + ':554/stream'

#inputname = 'kens-webcam'
#inputname = 'guest-checkin'
inputname = 'room-service-hallway'

# set url to 0 for webcam, otherwise mp4 file name
ip_camera_url = inputdir + inputname + '.mp4'

#ip_camera_url = 0
