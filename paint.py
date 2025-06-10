import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set (10, 150)

# myColors 

def findColor(img, myColors): # find color in the webcam
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array(myColors[0][0:3])
    upper = np.array(myColors[0][3:6])
    mask = cv2.inRange(imgHSV, lower, upper)
    cv2.imshow("mask", mask)
    

while True:
    success, img = cap.read()
    cv2.imshow("capture", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break