import cv2 as cv

image_path = cv.imread("C:/Users/Lenovo/Pictures/Saved Pictures/1-fishing-boats.jpg")
aa= image_path[100:300,200:400,2]
b = cv.cvtColor(image_path, cv.COLOR_BGR2GRAY)

# cv.imshow("Original", a)
# cv.imshow("Gray", b)
cv.imshow("Sliced", aa)
cv.waitKey(0)
cv.destroyAllWindows()