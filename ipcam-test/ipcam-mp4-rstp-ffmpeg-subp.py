'''
To connect and use FFmpeg, follow these steps:
Installation:
On Windows, download FFmpeg, extract the files, and add the FFmpeg directory to your system's PATH environment variable25.
On Linux or macOS, use package managers like apt or brew to install FFmpeg2.

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

input_file = '/path/to/input.mp4'
output_rtsp = 'rtsp://localhost:8554/live.sdp'

ffmpeg_command = [
    'ffmpeg',
    '-re',
    '-i', input_file,
    '-c:v', 'libx264',
    '-preset', 'ultrafast',
    '-f', 'rtsp',
    '-rtsp_transport', 'tcp',
    output_rtsp
]

subprocess.run(ffmpeg_command)