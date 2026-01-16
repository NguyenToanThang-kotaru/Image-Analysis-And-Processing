import cv2 as cv
import numpy as np
import math

width = height = 600
Task4 = np.ones((height, width), dtype=np.uint8) * 255

# Cirkle
centerCirkle = (height // 2, int(width * 1/4))
r = width // 8

for y in range(height):
    for x in range(width):
        d = math.sqrt((x - centerCirkle[1])**2 + (y - centerCirkle[0])**2)
        if abs(d - r) <= 1:
            Task4[y, x] = 0


## Square
centerSquare = (height // 2, int(width * 3/4))
sy, sx = centerSquare
side = width*1//4
half = side // 2

y, x = sy - half, sx - half  

directions = [
    (1, 0),   # down
    (0, 1),   # right
    (-1, 0),  # up
    (0, -1)   # left
]

for dy, dx in directions:
    for _ in range(side):
        if 0 <= y < height and 0 <= x < width:
            Task4[y, x] = 0
        y += dy
        x += dx


cv.imshow("CIRCLE OUT SQUARE", Task4)
cv.waitKey(0)
cv.destroyAllWindows()
