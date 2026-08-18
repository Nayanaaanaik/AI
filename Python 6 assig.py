import cv2

# Read the image
img = cv2.imread(r"C:\Users\nayan\Downloads\Flower.jpg")

# Check whether the image is loaded
if img is None:
    print("Error: Image could not be loaded.")
else:
    print("Shape :", img.shape)
    print("Size :", img.size)
    print("Data Type :", img.dtype)