import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

def preProcessing(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)
    imgCanny = cv2.Canny(imgBlur, 200, 200)
    kernel = np.ones((5,5))
    imgDial = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThres = cv2.erode(imgDial, kernel, iterations=1)
    return imgThres

def getContours(img, imgContour):
    biggest = np.array([])
    maxArea = 0
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 50:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            if area > maxArea and len(approx) == 4:  # find the biggest rectangle
                biggest = approx
                maxArea = area
    if biggest.size != 0:
        cv2.drawContours(imgContour, [biggest], -1, (255, 0, 0), 10)
    return biggest

def reorderPoints(pts):
    pts = pts.reshape((4, 2))
    new_pts = np.zeros((4,1,2), np.int32)
    add = pts.sum(1)
    new_pts[0] = pts[np.argmin(add)]  # top-left
    new_pts[3] = pts[np.argmax(add)]  # bottom-right
    diff = np.diff(pts, axis=1)
    new_pts[1] = pts[np.argmin(diff)]  # top-right
    new_pts[2] = pts[np.argmax(diff)]  # bottom-left
    return new_pts

def getWarp(img, biggest):
    if biggest.size != 0:
        try:
            biggest = reorderPoints(biggest)
            pts1 = np.float32(biggest)
            pts2 = np.float32([[0, 0], [frameWidth, 0], [0, frameHeight], [frameWidth, frameHeight]])
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            imgOutput = cv2.warpPerspective(img, matrix, (frameWidth, frameHeight))
            return imgOutput
        except:
            return img
    return img

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    imgContour = img.copy()
    imgThres = preProcessing(img)
    biggest = getContours(imgThres, imgContour)
    if biggest.size != 0:
        imgWarped = getWarp(img, biggest)  # warp the image if document is detected
        imageArray = ([img, imgThres], [imgContour, imgWarped])
    else:
        imageArray = ([img, imgThres], [imgContour, img])
    stackedImages = stackImages(0.6, imageArray)
    cv2.imshow("Scanned", stackedImages)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



