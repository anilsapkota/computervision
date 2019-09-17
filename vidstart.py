import numpy as np
import cv2

#create a video capture object and read in input file and check to see if it can open the file

cap = cv2.VideoCapture(0)   #'../images/shore.mov'

if cap.isOpened()==False:
    print('Cannot open file or Video')

while True:
    ret,frame = cap.read()

    if ret == True:
        cv2.imshow('Frame',frame)

        if cv2.waitKey(25) & 0xFF ==27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
