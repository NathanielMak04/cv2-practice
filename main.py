import cv2
import numpy as np

#img = cv2.imread("C:/Users/admin/Desktop/cv-practice/cv2-practice/images/f22.jpg")
vid = cv2.VideoCapture(0)\
vid.set(3,640)
vid.set(4,480)

#cv2.imshow("Image", img)
#cv2.waitKey(0)

while True:
    ret, frame = vid.read()
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


