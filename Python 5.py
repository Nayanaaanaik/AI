import cv2

cap = cv2.VideoCapture(0)

drawing = False
ix, iy = -1, -1
canvas = None


def draw(event, x, y, flags, param):
    global drawing, ix, iy, canvas

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(canvas, (ix, iy), (x, y),
                     (255, 0, 0), 4)
            ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


cv2.namedWindow("Camera")
cv2.setMouseCallback("Camera", draw)

while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera not detected")
        break

    # Create drawing canvas
    if canvas is None:
        canvas = frame.copy()

    # Show drawing on camera
    display = frame.copy()

    # Add canvas and camera together
    mask = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(mask, 10, 255, cv2.THRESH_BINARY)

    display[mask > 0] = canvas[mask > 0]

    cv2.imshow("Camera", display)

    key = cv2.waitKey(1) & 0xFF

    # C = Capture
    if key == ord('c'):
        cv2.imwrite("captured_image.jpg", display)
        print("Image Captured Successfully!")

    # E = Erase writing
    elif key == ord('e'):
        canvas = frame.copy()

    # Q = Quit
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()