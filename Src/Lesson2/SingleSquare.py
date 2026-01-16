import cv2 as cv
import numpy as np


width = height = 400
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
        # Task2[x,y] = 0
        side -= 1
        x += dx
        y += dy
        xy = x,y
        ListEdge.append(xy)

    side = 200

# Fill background
# Xác định các giới hạn của hình vuông từ các biến đã có
x_min, x_max = start_x, start_x + 200
y_min, y_max = start_y, start_y + 200

# Tô màu vùng (Fill region R)
# Theo lý thuyết, vùng R là tập hợp các pixel liên thông [2]
for i in range(x_min, x_max + 1):
    for j in range(y_min, y_max + 1):
        Task2[i, j] = 0  # Gán mức xám thấp nhất (màu đen) [3]

# for x,y in ListEdge:
    
#### Show image
cv.imshow("Task 2", Task2)
cv.waitKey(0)
cv.destroyAllWindows()