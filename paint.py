import cv2
import numpy as np
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set (10, 150)

myColors = [[42, 63, 83, 255, 90, 255],
            [42, 122, 95, 189, 72, 255]]

myColorValues = [[0, 255, 0],
                 [0, 0, 255]]

myPoints = []  # initialize as empty list

def findColor(img, myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV", imgHSV)
    newPoints = []
    count = 0
    
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        colored_mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        cv2.imshow("mask", colored_mask)
        x, y = getContours(mask, imgResult)
        if x != 0 and y != 0:  # only draw circle if we found a contour
            cv2.circle(imgResult, (x,y), 10, myColorValues[count], cv2.FILLED)
            newPoints.append([x, y, count])
        count += 1
    return newPoints

def getContours(imgMask, imgOriginal):
    contours, hierarchy = cv2.findContours(imgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 20:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgOriginal, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.drawContours(imgOriginal, [cnt], -1, (0, 255, 0), 2)
            return x+w//2, y  # return center point of the contour
    
    return 0, 0 

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)
    cv2.imshow("capture", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break