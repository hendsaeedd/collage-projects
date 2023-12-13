img = cv2.imread('img.jpg')

cv2.imshow('original',img )

width, height = 700, 500

pts1 = np.float32([[800, 551], [527, 622], [356, 364], [298, 967]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
img2 = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Perspective", img2)

cv2.waitKey(0)