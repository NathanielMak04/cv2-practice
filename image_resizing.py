import cv2
import numpy as np

img = cv2.imread("C:/Users/admin/Desktop/cv-practice/cv2-practice/images/f22.jpg")
print(img.shape)

imgResize = cv2.resize(img, (2180, 400))
print(imgResize.shape)

imgCropped = img[0:200, 200:500]
print(imgCropped.shape)

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)

