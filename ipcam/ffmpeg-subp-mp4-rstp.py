# py -m pip install ffmpeg-python


'''
To connect and use FFmpeg, follow these steps:
Installation:
1. download FFmpeg, extract the files, and add the FFmpeg directory to your system's PATH environment variable25.
On Linux or macOS, use package managers like apt or brew to install FFmpeg2.
2. on windows add ffmpeg\bin directory to system env path

Basic Usage:
Open a terminal or command prompt.
Run commands like ffmpeg -i input.mp4 output.avi to convert files3

Streaming Setup:
Configure FFmpeg for streaming by setting up an ffserver or using direct streaming commands14.

Configure Streaming:
Use the following command to capture video from your IP camera and stream it:
bash
ffmpeg -i rtsp://<camera-ip>:<port>/stream -c:v copy -f flv rtmp://<server-ip>/live/stream

Replace <camera-ip>, <port>, and <server-ip> with your camera's IP, port, and streaming server details.


FFmpeg with Python subprocess:
You can use FFmpeg, a powerful multimedia framework, through Python's subprocess module to convert MP4 to RTSP. 
While not a pure Python solution, it's effective:
'''
import subprocess
import sys
import importlib
import ffmpeg
#from ffmpeg import FFmpeg

# https://github.com/kkroening/ffmpeg-python

debug = True

sys.path.append('inputs')
module = importlib.import_module('video-inout-settings')
ip_camera_url = module.ip_camera_url
print('video source: ' + ip_camera_url)

# doesn't work: 
#sys.path.append(r"C:\Users\kjcot\ffmpeg\bin")
#ffmpeg.FFMPEG_BINARY = r"C:\Users\kjcot\ffmpeg\bin\ffmpeg.exe"
# only thing that works is to add ffmpeg bin directory to sys path in Environment
ip_camera_url = module.ip_camera_url

print('reading this MP4 file: ' + str(ip_camera_url))

outputfile = module.outputdir + 'output1.mp4'
output_rtsp = 'rtsp://localhost:554/ken'

#ffmpeg.input(ip_camera_url).hflip().output(output_rtsp).run()
'''
  ffmpeg = (
        FFmpeg()
        .option("y")
        .input(ip_camera_url)
        .output(outputfile),
        {"codec:v": "libx264"},
        vf="scale=1280:-1",
        preset="veryslow",
        crf=24)
    )
    ))
    ffmpeg.execute()
'''
  
debug = True
if debug:
    ffmpeg_command = [
        'ffmpeg',
        '-re',
        '-i', ip_camera_url,
        '-c:v', 'libx264',
        '-preset', 'ultrafast',
        '-f', 'rtsp',
        '-rtsp_transport', 'tcp',
        output_rtsp
    ]

    subprocess.run(ffmpeg_command)