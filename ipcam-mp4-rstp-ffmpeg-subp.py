'''
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