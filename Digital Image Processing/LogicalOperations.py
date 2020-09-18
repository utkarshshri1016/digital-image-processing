from cv2 import cv2
img1=cv2.imread("Resources/Data/lena.png")
img2=cv2.imread("Resources/Data/baboon.jpg")
imgand = cv2.bitwise_and(img1,img2)
imgor= cv2.bitwise_or(img1,img2)
imgxor= cv2.bitwise_xor(img1,img2)
cv2.imshow("AND Image",imgand)
cv2.imshow("OR Image",imgor)
cv2.imshow("XOR Image",imgxor)
cv2.waitKey()