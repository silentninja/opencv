import cv2
import numpy
import os
#random bytes for the img
randomByteArray = bytearray(os.urandom(120000))
flatnumpyarr = numpy.array(randomByteArray)
grayimage= flatnumpyarr.reshape(300,400)
cv2.imwrite('randgra.png',grayimage)
bgrimg = flatnumpyarr.reshape(100,400,3)
cv2.imwrite('randimg.png',bgrimg)