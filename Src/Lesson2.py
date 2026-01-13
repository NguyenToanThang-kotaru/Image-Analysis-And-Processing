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

width = height = 400
# Task1 = np.ones((width, height), dtype=np.uint8) * 255
# r = 100
# xc,yc = 200,200
# d = 0

# ##### Draw a cirkle
# for y in range(height):
#     for x in range(width):
#         d= math.sqrt((x-xc)**2+(y-yc)**2)
#         if(r-1<d<r+1):
#             Task1[y,x] = 0

# ##### Fill the background
# for y in range(height):
#     for x in range(width):
#         d= math.sqrt((x-xc)**2+(y-yc)**2)
#         if(d<r):
#             Task1[y,x]=0

# cv.imshow("Binary", Task1)
# cv.waitKey(0)
# cv.destroyAllWindows()

Task2 = np.ones((width,height),dtype=np.uint8)*255

centerPoint =int(width/2),int(height/2)
side  = 200

start_x, start_y = int(centerPoint[0]/2),int(centerPoint[1]/2)
x,y = start_x,start_y

directions = [
    (0, 1),   # sang phải
    (1, 0),   # xuống
    (0, -1),  # sang trái
    (-1, 0)   # lên
]

ListEdge=[]
for dx,dy in directions:
    while (side!=0):
        Task2[x,y] = 0
        side -= 1
        x += dx
        y += dy
        xy = x,y
        ListEdge.append(xy)

    side = 200

# for x,y in ListEdge:
    
#### Show image
cv.imshow("Task 2", Task2)
cv.waitKey(0)
cv.destroyAllWindows()