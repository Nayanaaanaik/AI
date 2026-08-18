import cv2 as cv
import os

# Path of your bike video
video_path = r"C:\Users\nayan\Downloads\13010564_1920_1080_60fps.mp4"

# Folder to save extracted frames
output_folder = "Extracted_Frames"

# Create folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Open video
cap = cv.VideoCapture(video_path)

# Check whether video opened
if not cap.isOpened():
    print("Error: Cannot open video file")
    exit()

frame_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Save each frame
    filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
    cv.imwrite(filename, frame)

    frame_count += 1

cap.release()

print("Frame Extraction Completed Successfully!")
print("Total Frames Extracted:", frame_count)
print("Frames are saved in the 'Extracted_Frames' folder.")