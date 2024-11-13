import os
inputfile = r"C:\Users\kjcot\mp4files\guest-checkin.mp4"
outputfile = "output6.mp4"
command = 'ffmpeg -i' + " " + inputfile + " " + outputfile
print('command: ' + command)
os.system(command)

# os.system("ffmpeg -i rtsp://192.168.1.100/stream -codec copy -f h264 output.mp4 -codec copy -f mpegts udp://127.0.0.1:3000 &")