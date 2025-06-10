import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set (10, 150)

myColors = [[46, 179, 73, 157, 63, 210],
            [42, 122, 95, 189, 72, 255]]

def findColor(img, myColors): # find color in the webcam
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        getContours(mask, imgResult)
        cv2.imshow("mask", mask)

def getContours(imgMask, imgOriginal):
    contours, hierarchy = cv2.findContours(imgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 50:  # only process contours with significant area
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            # draw bounding box in red
            cv2.rectangle(imgOriginal, (x, y), (x+w, y+h), (0, 0, 255), 2)
            # draw contour in green
            cv2.drawContours(imgOriginal, [cnt], -1, (0, 255, 0), 2)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    findColor(img, myColors)
    cv2.imshow("capture", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break