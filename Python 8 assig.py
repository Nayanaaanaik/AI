import cv2

# Read the image
img = cv2.imread(r"C:\Users\nayan\Downloads\Uttarakannada.jpg")

# Check whether the image is loaded
if img is None:
    print("Error: Image could not be loaded.")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display the original and grayscale images
    cv2.imshow("Original Image", img)
    cv2.imshow("Grayscale Image", gray)

    # Save the grayscale image
    cv2.imwrite(r"C:\Users\nayan\Downloads\Uttarakannada_Gray.jpg", gray)

    print("Grayscale image saved successfully.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()