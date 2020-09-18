from cv2 import cv2
img=cv2.imread("Resources/Data/lena.png")
comp=255-img
cv2.imshow("Complemented image",comp)
cv2.waitKey()