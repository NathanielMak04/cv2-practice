import cv2
import numpy as np

#img = cv2.imread("C:/Users/admin/Desktop/cv-practice/cv2-practice/images/f22.jpg")
img = cv2.imread("C:/Users/Nathaniel/Desktop/augmented-reality-app/images/f22.jpg")

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # convert to HSV
