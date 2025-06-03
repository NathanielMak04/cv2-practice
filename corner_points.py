import cv2
import numpy as np

img = cv2.imread("images/f22.jpg")


# convert to grayscale so that we can detect edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred_img = cv2.GaussianBlur(gray, (5, 5), 1)


# detect edges
edges = cv2.Canny(blurred_img, 50, 150)

# detect corners
corners = cv2.goodFeaturesToTrack(edges, 100, 0.01, 10)

# draw corners
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)   



img_stack = stackImages(0.7, ([img, gray, blurred_img]))

cv2.imshow("Image", img_stack)
cv2.waitKey(0)





