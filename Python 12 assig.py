import cv2 as cv

# Path to your bike video
video_path = r"C:\Users\nayan\Downloads\13010564_1920_1080_60fps.mp4"

cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video file")
    exit()

ret, frame = cap.read()

if not ret:
    print("Cannot read video")
    exit()

# Select object to track
bbox = cv.selectROI("Select Object", frame, fromCenter=False, showCrosshair=True)
cv.destroyWindow("Select Object")

# Create MIL Tracker
tracker = cv.TrackerMIL_create()
tracker.init(frame, bbox)

print("Object Tracking Started...")
print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    success, bbox = tracker.update(frame)

    if success:
        x, y, w, h = [int(v) for v in bbox]
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv.putText(frame, "Tracking", (x, y - 10),
                   cv.FONT_HERSHEY_SIMPLEX, 0.7,
                   (0, 255, 0), 2)
    else:
        cv.putText(frame, "Tracking Failure", (30, 50),
                   cv.FONT_HERSHEY_SIMPLEX, 0.8,
                   (0, 0, 255), 2)

    cv.imshow("Object Tracking", frame)

    if cv.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

print("Object Tracking Completed Successfully!")