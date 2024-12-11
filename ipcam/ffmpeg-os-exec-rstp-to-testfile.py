import os
import sys
import importlib



sys.path.append('inputs')  # directory of module
module = importlib.import_module('video-inout-settings')  # module name
ip_cameral_url = module.ip_camera_url

#inputfile = r"C:\Users\kjcot\mp4files\guest-checkin.mp4"
# outputfile = "output6.mp4"

'''
ffmpeg -i input.mp4 -rtsp_transport tcp -c:v libx264 -preset ultrafast -tune zerolatency \
    -b:v 500k -c:a aac -strict experimental -f rtsp rtsp://your_server_address:your_port/live

    
ffmpeg -i rtsp://<camera-ip>:<port>/stream -c:v copy -f flv rtmp://<server-ip>/live/stream    
    
https://www.dacast.com/blog/how-to-broadcast-live-stream-using-ffmpeg/

https://trac.ffmpeg.org/wiki/StreamingGuide

'''
rstpin  = module.output_rstp

command = 'ffmpeg -i' + " " + ip_cameral_url + "  -f rtsp -rtsp_transport tcp  " + rstpout
command = "ffmpeg -i " + rstpin  + " -codec copy -f h264 " + output.mp4 -codec copy -f mpegts udp://127.0.0.1:3000"

print('command: ' + command)
os.system(command)

# os.system("ffmpeg -i rtsp://192.168.1.100/stream -codec \
#  copy -f h264 output.mp4 -codec copy -f mpegts udp://127.0.0.1:3000 &")