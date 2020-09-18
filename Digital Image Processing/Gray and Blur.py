from cv2 import cv2
img=cv2.imread("Resources/Data/lena.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(img,(31,31),0)
cv2.imshow("Gray Image",gray)
cv2.imshow("Blurred Image",blur)
cv2.waitKey()