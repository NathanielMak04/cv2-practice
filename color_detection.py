import cv2
import numpy as np

def empty(a):
    pass

# Create trackbar window
cv2.namedWindow("trackbar")
cv2.resizeWindow("trackbar",640, 240)
cv2.createTrackbar("Hue Min", "trackbar", 0, 179, empty)
cv2.createTrackbar("Hue Max", "trackbar", 179, 179, empty)
cv2.createTrackbar("Sat Min", "trackbar", 0, 255, empty)
cv2.createTrackbar("Sat Max", "trackbar", 255, 255, empty)
cv2.createTrackbar("Val Min", "trackbar", 0, 255, empty)
cv2.createTrackbar("Val Max", "trackbar", 255, 255, empty)

while True:
    # Read image
    img = cv2.imread("images/f22.jpg")
    if img is None:
        print("Error: Could not load image")
        break
    
    # Convert to HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Get trackbar positions
    h_min = cv2.getTrackbarPos("Hue Min", "trackbar")
    h_max = cv2.getTrackbarPos("Hue Max", "trackbar")
    s_min = cv2.getTrackbarPos("Sat Min", "trackbar")
    s_max = cv2.getTrackbarPos("Sat Max", "trackbar")
    v_min = cv2.getTrackbarPos("Val Min", "trackbar")
    v_max = cv2.getTrackbarPos("Val Max", "trackbar")
    
    # Create mask
    mask = cv2.inRange(imgHSV, (h_min, s_min, v_min), (h_max, s_max, v_max))
    
    # Show images
    cv2.imshow("Image", img)
    cv2.imshow("Image HSV", imgHSV)
    cv2.imshow("Mask", mask)
    
    # Break loop with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()