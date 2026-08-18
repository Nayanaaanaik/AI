import cv2 as cv

# Full path of your video
video_path = r"C:\Users\nayan\Downloads\13010564_1920_1080_60fps.mp4"

# Open the video
cap = cv.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Cannot open video file")
    exit()

print("Video opened successfully.")
print("Press 'q' to quit.")

while True:
    # Read one frame
    ret, frame = cap.read()

    # Stop when the video ends
    if not ret:
        print("End of video.")
        break

    # Display the frame
    cv.imshow("Bike Video", frame)

    # Press q to exit
    if cv.waitKey(30) & 0xFF == ord('q'):
        print("Video stopped by user.")
        break

# Release resources
cap.release()
cv.destroyAllWindows()

print("Program terminated successfully.")