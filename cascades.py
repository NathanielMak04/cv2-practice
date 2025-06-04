import cv2

face_cascade = cv2.CascadeClassifier("cascades/haarcascade_frontalface_default.xml")
img = cv2.imread("images/face.jpg")


scale_percent = 800 / img.shape[1]  # calculate scale percentage based on desired width
width = 800
height = int(img.shape[0] * scale_percent)
dim = (width, height)
img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)

