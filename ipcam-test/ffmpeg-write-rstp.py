import ffmpeg

# Define your input source 
input_source = 'your_video_file.mp4' # Replace with your video file or other input source

# Create the FFmpeg command
(
    ffmpeg
    .input(input_source)
    .output('rtsp://localhost:8554/mystream', format='rtsp', vcodec='libx264', acodec='aac')
    .run_async(pipe_stdout=True, pipe_stderr=True)
)