import cv2

img = cv2.imread("C:/Users/admin/Desktop/cv-practice/cv2-practice/images/f22.jpg")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(imgBlur, 100, 150)
imgDilation = cv2.dilate(imgCanny, (3,3), iterations=1)
imgEroded = cv2.erode(imgDilation, (3,3), iterations=1)

cv2.imshow("Image", img)
cv2.imshow("Image Gray", imgGray)
cv2.imshow("Image Blur", imgBlur)
cv2.imshow("Image Canny", imgCanny)
cv2.imshow("Image Dilation", imgDilation)
cv2.imshow("Image Eroded", imgEroded)
cv2.waitKey(0)


