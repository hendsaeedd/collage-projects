import cv2 as cv

img = cv.imread("img.png")
cv.imshow("Original Image", img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Threshold Image", thresh)
threshold1, thresh1 = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Threshold Image inv", thresh1)

#Adaptive Thresholding
adaptive_mean = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow("Adaptive Mean", adaptive_mean)
adaptive_gaussian = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow("Adaptive Gaussian", adaptive_gaussian)
cv.waitKey(0)