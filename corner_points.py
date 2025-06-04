import cv2
import numpy as np

def stackImages(scale, imgArray):
    """
    this function helps to display multiple images side by side
    scale - how much to resize the images (0.7 means 70% of original size)
    imgArray - list of images to display
    """
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                # resize images to match the first image's size
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                # convert grayscale to color (BGR) so we can stack them together
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])  # stack images horizontally
        ver = np.vstack(hor)  # stack the rows vertically
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)  # stack images horizontally
        ver = hor
    return ver

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print(f"Found {len(contours)} contours")
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # draw all contours in blue first
        cv2.drawContours(img_contour, cnt, -1, (255, 0, 0), 2)
        
        if area > 50: 
            # draw significant contours in green
            cv2.drawContours(img_contour, cnt, -1, (0, 255, 0), 2) 
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(f"Contour - Area: {area:.2f}, Perimeter: {peri:.2f}, Corners: {len(approx)}")
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(img_contour, (x, y), (x+w, y+h), (0, 0, 255), 2) 
            

            if objCor == 3:
                myobj = "Triangle"
            elif objCor == 4:
                myobj = "Rectangle"
            elif objCor == 5:
                myobj = "Pentagon"
            elif objCor > 5:
                myobj = "Circle"
            else:
                myobj = "None"

            cv2.putText(img_contour, myobj, (x+(w//2), y+(h//2)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
                


# read the image from file
# imread converts the image into a numpy array that we can work with
img = cv2.imread("images/shapes.jpg")
img_contour = img.copy()

# convert the image from RGB to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur the image to reduce noise
blurred_img = cv2.GaussianBlur(gray, (5, 5), 1)


edges = cv2.Canny(blurred_img, 50, 150)
getContours(edges)
corners = cv2.goodFeaturesToTrack(edges, 100, 0.01, 10)

# draw circles at each corner point we found
for corner in corners:
    x, y = corner.ravel()  # flatten the array from [[x,y]] to [x,y]
    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)   

# make scale 1.2 to show images at 120% of their original size
img_stack = stackImages(1.5, ([img, gray, blurred_img, edges, img_contour]))

cv2.imshow("Image", img_stack)

cv2.waitKey(0)





