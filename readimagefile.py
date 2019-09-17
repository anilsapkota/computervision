import numpy as np
import cv2
img = cv2.imread('../images/anil.jpg') #this is path to the image file 
#print(img.shape)

b = img[:,:,0] #all of the row , all of the coloumn , first array as 0
print(b)

g = img[:,:,1]
r = img[:,:,2]

cv2.imshow('Blue', b)
cv2.imshow('Green',g)
cv2.imshow('red', r)

cv2.imshow('Image', img) #this command displays the Image read from the imread command 

cv2.waitKey(0)
cv2.destroyAllWindows() 
