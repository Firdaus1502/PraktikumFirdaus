import cv2
import numpy as np


img = cv2.imread("IMG DAUS.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("gambar IMG DAUS original", img)
cv2.imshow("gambar IMG DAUS grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()