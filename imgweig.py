import cv2
import cv
image= cv2.imread('fruits.jpg')
image2= cv2.imread('fruits.jpg')
cv.NamedWindow('my window', cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow('original', cv.CV_WINDOW_AUTOSIZE)
b,g,r = cv2.split(image)
cv2.addWeighted(b,0.5,g,0.5,0,b)
cv2.merge((b,b,r),image)

cv2.imshow('my window',image)
cv2.imshow('original',image2)
cv.WaitKey()




