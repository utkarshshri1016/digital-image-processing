from cv2 import cv2
img1=cv2.imread("Resources/Data/lena.png",0)
img2=cv2.imread("Resources/Data/baboon.jpg",0)
ad=img1+img2
sub=img1-img2
div=img1/img2
multi=img1*img2
cv2.imshow("Addition Image",ad)
cv2.imshow("Subtraction Image",sub)
cv2.imshow("Multiplication Image",multi)
cv2.imshow("Division Image",div)
cv2.waitKey()