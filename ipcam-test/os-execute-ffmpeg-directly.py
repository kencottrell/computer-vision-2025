import os
os.system("ffmpeg -i rtsp://192.168.1.100/stream -codec copy -f h264 output.mp4 -codec copy -f mpegts udp://127.0.0.1:3000 &")