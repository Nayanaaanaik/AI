import cv2

# Open webcam
camera = cv2.VideoCapture(0)

# Check if webcam opened successfully
if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    # Read frame from webcam
    ret, frame = camera.read()

    if not ret:
        print("Failed to capture image.")
        break

    # Display webcam feed
    cv2.imshow("Web Camera", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close all windows
camera.release()
cv2.destroyAllWindows()