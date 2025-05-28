import cv2
import numpy as np

#img = cv2.imread("C:/Users/admin/Desktop/cv-practice/cv2-practice/images/f22.jpg")
img = cv2.imread("C:/Users/Nathaniel/Desktop/augmented-reality-app/images/f22.jpg")

width,height = 200,200
pts1 = np.float32([[19,14],[253,14],[19,139],[253,139]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)

result = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image", img)
cv2.imshow("Result", result)
cv2.waitKey(0)

