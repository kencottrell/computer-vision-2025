import ffmpeg
import sys
import importlib


sys.path.append('inputs')
module = importlib.import_module('video-input-settings')
ip_cameral_url = module.ip_camera_url

# Define your input source 
input_source = 'your_video_file.mp4' # Replace with your video file or other input source

# Create the FFmpeg command
(
    ffmpeg
    .input(ip_cameral_url)
    .output('rtsp://localhost:8554/mystream', format='rtsp', vcodec='libx264', acodec='aac')
    .run_async(pipe_stdout=True, pipe_stderr=True)
)