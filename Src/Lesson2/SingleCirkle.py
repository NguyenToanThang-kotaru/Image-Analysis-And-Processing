import cv2 as cv
import numpy as np
import math


width = height = 400
Task1 = np.ones((width, height), dtype=np.uint8) * 255
r = 100
xc,yc = 200,200
d = 0

##### Draw a cirkle
for y in range(height):
    for x in range(width):
        d= math.sqrt((x-xc)**2+(y-yc)**2)
        if(r-1<d<r+1):
            Task1[y,x] = 0

##### Fill the background
for y in range(height):
    for x in range(width):
        d= math.sqrt((x-xc)**2+(y-yc)**2)
        if(d<r):
            Task1[y,x]=0

cv.imshow("Binary", Task1)
cv.waitKey(0)
cv.destroyAllWindows()
