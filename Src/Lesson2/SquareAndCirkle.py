import cv2 as cv
import numpy as np
import math

width = height = 400
Task3 = np.ones((width,height), dtype= np.uint8)*255
center = (height // 2, width // 2)
r = 100

Task3[center[0], center[1]] = 0
for y in range(0,height,1):
    for x in range(0,width,1):
        d= math.sqrt((x-center[0])**2+(y-center[1])**2)
        if(r-1<d<r+1):
            Task3[y,x] = 0

side = 200
directions = [
    (0, 1),   # sang phải
    (1, 0),   # xuống
    (0, -1),  # sang trái
    (-1, 0)   # lên
]
x,y = (center[0]//2,center[1]//2 )
for dx,dy in directions:
    for side in range(0,side,1):
       Task3[x,y]=0
       x = x+dx
       y = y+dy
        

cv.imshow("CIRKLE IN SQUARE",Task3)
cv.waitKey(0)
cv.destroyAllWindows()