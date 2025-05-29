import cv2
import numpy as np

img = cv2.imread("C:/Users/admin/Desktop/cv-practice/cv2-practice/images/f22.jpg")
#img = cv2.imread("C:/Users/Nathaniel/Desktop/augmented-reality-app/images/f22.jpg")

def empty(a):
    pass

cv2.namedWindow("trackbar")
cv2.resizeWindow("trackbar",640, 240)
cv2.createTrackbar("Hue Min", "trackbar", 0, 179,empty)
cv2.createTrackbar("Hue Max", "trackbar", 179, 179,empty)
cv2.createTrackbar("Sat Min", "trackbar", 0, 255,empty)
cv2.createTrackbar("Sat Max", "trackbar", 255, 255,empty)
cv2.createTrackbar("Val Min", "trackbar", 0, 255,empty)
cv2.createTrackbar("Val Max", "trackbar", 255, 255,empty)

while True:
    img = cv2.imread("C:/Users/admin/Desktop/cv-practice/cv2-practice/images/f22.jpg")
    h_min = cv2.getTrackbarPos("Hue Min", "trackbar")
    h_max = cv2.getTrackbarPos("Hue Max", "trackbar")
    s_min = cv2.getTrackbarPos("Sat Min", "trackbar")
    s_max = cv2.getTrackbarPos("Sat Max", "trackbar")
    v_min = cv2.getTrackbarPos("Val Min", "trackbar")
    v_max = cv2.getTrackbarPos("Val Max", "trackbar")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    




imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert to HSV

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])


cv2.imshow("Image", img)
cv2.imshow("Image HSV", imgHSV)

cv2.waitKey(0)

