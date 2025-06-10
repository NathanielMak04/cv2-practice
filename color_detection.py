import cv2
import numpy as np

def empty(a):
    pass

# initialize video capture
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set (10, 150)


# create trackbar window
cv2.namedWindow("trackbar")
cv2.resizeWindow("trackbar",640, 240)
cv2.createTrackbar("Hue Min", "trackbar", 0, 179, empty)
cv2.createTrackbar("Hue Max", "trackbar", 179, 179, empty)
cv2.createTrackbar("Sat Min", "trackbar", 0, 255, empty)
cv2.createTrackbar("Sat Max", "trackbar", 255, 255, empty)
cv2.createTrackbar("Val Min", "trackbar", 0, 255, empty)
cv2.createTrackbar("Val Max", "trackbar", 255, 255, empty)

while True:
    # read image
    success, img = cap.read()
    cv2.imshow("capture", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # convert to HSV
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
    
    # get trackbar positions
    h_min = cv2.getTrackbarPos("Hue Min", "trackbar") # get the position of the trackbar
    h_max = cv2.getTrackbarPos("Hue Max", "trackbar")
    s_min = cv2.getTrackbarPos("Sat Min", "trackbar")
    s_max = cv2.getTrackbarPos("Sat Max", "trackbar")
    v_min = cv2.getTrackbarPos("Val Min", "trackbar")
    v_max = cv2.getTrackbarPos("Val Max", "trackbar")
    
    # create mask
    mask = cv2.inRange(imgHSV, (h_min, s_min, v_min), (h_max, s_max, v_max)) # filter to show which pixels are in the range; white pixels are in the range; black pixels are not in the range
    
    # Show images
    cv2.imshow("Image HSV", imgHSV)
    cv2.imshow("Mask", mask)
    
    # break loop with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()