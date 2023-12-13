import cv2 as cv

img = cv.imread(r"example.jpg")
cv.imshow("t", img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grey", grey)

gauss = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow("gauss", gauss)
avg = cv.blur(img, (3, 3))
cv.imshow("blur", avg)
bilateral = cv.bilateralFilter(img, 5, 35, 25)
cv.imshow("bilateral", bilateral)

img2 = cv.imread("download.jpeg")
cv.imshow("salt&peper", img2)
median = cv.medianBlur(img2, 3)
cv.imshow("median", median)

cv.waitKey(0)
