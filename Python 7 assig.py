import cv2

# Read the image
img = cv2.imread(r"C:\Users\nayan\Downloads\flowers.jpg")

if img is None:
    print("Error: Image could not be loaded.")
else:
    # Crop the image
    crop = img[20:120, 20:120]

    # Resize the cropped image
    resized = cv2.resize(crop, (200, 200))

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Cropped Image", crop)
    cv2.imshow("Resized Image", resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()