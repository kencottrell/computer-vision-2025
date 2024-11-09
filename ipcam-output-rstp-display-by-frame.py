import cv2

# Replace with your RTSP stream URL
rtsp_url = 'rtsp://username:password@ip_address:port/endpoint'

# Open the RTSP stream
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Error: Cannot open RTSP stream")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Display the resulting frame
    cv2.imshow('RTSP Stream', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()