import cv2 as cv

img = cv.imread(r"example.jpg")
cv.imshow("t", img)

canny = cv.Canny(img, 125, 175)
cv.imshow("canny", canny)

dilate = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow("dilate", dilate)

erode = cv.erode(canny, (3, 3), iterations=1)
cv.imshow("erode", erode)

crop = img[50:100, 200:400]
cv.imshow("crop", crop)
cv.waitKey(0)