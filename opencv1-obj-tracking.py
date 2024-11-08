import cv2

# Initialize video capture
cap = cv2.VideoCapture("video.mp4")  # Replace "video.mp4" with 0 for webcam

# Choose an object tracker
tracker = cv2.TrackerCSRT_create()  # Options: CSRT, KCF, BOOSTING, MIL, TLD, MEDIANFLOW, MOSSE, GOTURN

# Read the first frame
success, frame = cap.read()
if not success:
    print("Failed to read video")
    exit()

# Select a bounding box on the first frame
bbox = cv2.selectROI("Tracking", frame, False)

# Initialize the tracker with the first frame and bounding box
tracker.init(frame, bbox)

while True:
    # Read a new frame
    success, frame = cap.read()
    if not success:
        break

    # Update the tracker and get updated position
    success, bbox = tracker.update(frame)
    
    if success:
        # Draw bounding box
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2)
    else:
        cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Display result
    cv2.imshow("Tracking", frame)

    # Exit on ESC key
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()