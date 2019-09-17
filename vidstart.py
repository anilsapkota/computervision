import numpy as np
import cv2

#create a video capture object and read in input file and check to see if it can open the file

cap = cv2.VideoCapture('../images/shore.mov')   #use 0 in path if you want webcamera to capture

if cap.isOpened()==False:
    print('Cannot open file or Video')

while True:
    ret,frame = cap.read() #ret is return parameter

    if ret == True:
        cv2.imshow('Frame',frame)

        if cv2.waitKey(25) & 0xFF ==27:   #here on wait key we have to pass number >0 as 0 would pause
            break                         #open cv sugget to use at least 25 milliseconds
    else:
        break                             #if return is not true then we want to break

cap.release()                            # here we release the video capture object
cv2.destroyAllWindows()
