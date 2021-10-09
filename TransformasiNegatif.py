import cv2

img = cv2.imread("IMG DAUS.jpg", 0)

negatif = 255 - img

cv2.imshow("Original Image", img)
cv2.imshow("Image Negative", negatif)

cv2.waitKey(0)
cv2.destroyAllWindows()