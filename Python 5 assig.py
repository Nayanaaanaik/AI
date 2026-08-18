import cv2

# Read the image
img = cv2.imread(r"C:\Users\nayan\OneDrive\Pictures\Murudeshwara pic.jpg")

# Check whether the image is loaded
if img is None:
    print("Error: Image could not be loaded.")
else:
    print("Image loaded successfully.")

    # Display the image
    cv2.imshow("Murudeshwara Image", img)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()