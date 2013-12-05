import numpy
import cv2
import cv
image = cv2.imread('lena.jpg')
cv.NamedWindow('my window', cv.CV_WINDOW_AUTOSIZE)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('my window',image)
cv2.imshow('gray',gray)
cv.WaitKey()

