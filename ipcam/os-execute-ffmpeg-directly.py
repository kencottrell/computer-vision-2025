import os
import sys
import importlib



sys.path.append('inputs')  # directory of module
module = importlib.import_module('video-inout-settings')  # module name
ip_cameral_url = module.ip_camera_url

inputfile = r"C:\Users\kjcot\mp4files\guest-checkin.mp4"
outputfile = "output6.mp4"
command = 'ffmpeg -i' + " " + ip_cameral_url + " " + outputfile
print('command: ' + command)
os.system(command)

# os.system("ffmpeg -i rtsp://192.168.1.100/stream -codec copy -f h264 output.mp4 -codec copy -f mpegts udp://127.0.0.1:3000 &")