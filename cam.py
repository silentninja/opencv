import numpy as np
import cv2


    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        x = int(x)
        y = int(y)
        w = int(w)
        h = int (h)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        x = int(x)
        y = int(y)
        w = int(w)
        h = int (h)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
