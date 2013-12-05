import cv2
import cv
src = cv2.imread('building.jpg')
dst = cv2.imread('building.jpg')
cv.NamedWindow('edged', cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow('original', cv.CV_WINDOW_AUTOSIZE)
blurredSrc = cv2.medianBlur(src, 7)
graySrc = cv2.cvtColor(blurredSrc, cv2.cv.CV_BGR2GRAY)
cv2.Laplacian(graySrc, cv2.cv.CV_8U, graySrc, ksize = 5)
normalizedInverseAlpha = (1.0 / 255) * (255 - graySrc)
channels = cv2.split(src)
for channel in channels:
 channel[:] = channel * normalizedInverseAlpha
cv2.merge(channels, dst)
cv2.imshow('original',src)
cv2.imshow('edged',dst)
cv.WaitKey()





