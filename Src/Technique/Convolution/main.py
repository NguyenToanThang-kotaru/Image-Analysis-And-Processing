import cv2 as cv
import numpy as np
import os

BASE_DIR = os.path.dirname(__file__)
image_path = os.path.join(BASE_DIR, "..", "..", "..", "Images", "lena_std.tif")

image = cv.imread(image_path)
cv.imshow("Convoluation", image)
cv.waitKey(0)
cv.destroyAllWindows()