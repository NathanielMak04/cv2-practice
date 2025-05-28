import cv2
import numpy as np

#img = cv2.imread("C:/Users/admin/Desktop/cv-practice/cv2-practice/images/f22.jpg")
img = cv2.imread("C:/Users/Nathaniel/Desktop/augmented-reality-app/images/f22.jpg")

horizontal = np.hstack((img,img))
vertical = np.vstack((img,img))

cv2.imshow("Horizontal", horizontal)
cv2.imshow("Vertical", vertical)
cv2.waitKey(0)

