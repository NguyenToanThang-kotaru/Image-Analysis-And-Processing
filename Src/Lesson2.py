###### Import necessary library
import cv2 as cv
import numpy as np
import math
# image_path = cv.imread("C:/Users/Lenovo/Pictures/Saved Pictures/1-fishing-boats.jpg")
# aa= image_path[100:300,200:400,2]
# b = cv.cvtColor(a, cv.COLOR_BGR2GRAY)

# # cv.imshow("Original", a)
# # cv.imshow("Gray", b)
# cv.imshow("Sliced", aa)
# cv.waitKey(0)
# cv.destroyAllWindows()

width = height = 800
bg = np.ones((width, height), dtype=np.uint8) * 255
r = 100
xc,yc = 200,200
d = 0

##### Draw a cirkle
for y in range(height):
    for x in range(width):
        d= math.sqrt((x-xc)**2+(y-yc)**2)
        if(r-1<d<r+1):
            bg[y,x] = 0

##### Fill the background
for y in range(height):
    for x in range(width):
        d= math.sqrt((x-xc)**2+(y-yc)**2)
        if(d<r):
            bg[y,x]=0


cv.imshow("Binary", bg)
cv.waitKey(0)
cv.destroyAllWindows()


