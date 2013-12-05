import numpy as np
import cv2
import cv
threeDWinName = "3D View"
cv2.namedWindow(threeDWinName, cv2.CV_WINDOW_AUTOSIZE)
img2 = cv2.imread('lena.jpg')
cv2.circle(img2, (100,100),100,255,-1)

cv2.imshow(threeDWinName,img2)
cv.WaitKey()