from cv2 import cv2
img1=cv2.imread("Resources/Data/lena.png")
img2=cv2.imread("Resources/Data/baboon.jpg")
img=cv2.addWeighted(img2,0.3,img1,0.7,0)
cv2.imshow("Blended Image",img)
cv2.waitKey()