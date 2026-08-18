import cv2 as cv

# Path of your bike video
video_path = r"C:\Users\nayan\Downloads\13010564_1920_1080_60fps.mp4"

# Open the video
cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video file")
    exit()

# Create Background Subtractor
back_sub = cv.createBackgroundSubtractorMOG2(
    history=500,
    varThreshold=16,
    detectShadows=True
)

print("Motion Detection Started...")
print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Apply background subtraction
    fg_mask = back_sub.apply(frame)

    # Display original video
    cv.imshow("Original Video", frame)

    # Display foreground mask
    cv.imshow("Motion Detection", fg_mask)

    if cv.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

print("Motion Detection Completed Successfully!")