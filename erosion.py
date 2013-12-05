import cv2
import numpy as np
import cv
img = cv2.imread('lena.jpg',0)
img2 = cv2.imread('lena.jpg',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imshow('eroded',erosion)
cv2.imshow('img',img)
cv.WaitKey()
