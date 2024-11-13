import cv2
import ffmpeg

# Replace with your RTSP stream URL
rtsp_url = "rtsp://username:password@your_ip_address/your_stream"

# Open the RTSP stream
process = (
    ffmpeg
    .input(rtsp_url)
    .output("pipe:", format="rawvideo", pix_fmt="bgr24")
    .run_async(pipe_stdout=True)
)

# Read frames from the stream
while True:
    in_bytes = process.stdout.read(1920 * 1080 * 3)  # Adjust for your resolution
    if not in_bytes:
        break

    frame = np.frombuffer(in_bytes, np.uint8).reshape((1080, 1920, 3))  # Adjust for your resolution

    # Display the frame
    cv2.imshow("RTSP Stream", frame)

    if cv2.waitKey(1) == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
process.terminate()