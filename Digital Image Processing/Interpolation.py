from cv2 import cv2
img=cv2.imread("Resources/Data/baboon.jpg")
near_img = cv2.resize(img,None, fx = .7, fy = .7, interpolation = cv2.INTER_NEAREST)
bilinear_img = cv2.resize(img,None, fx = .7, fy = .7, interpolation = cv2.INTER_LINEAR) 
bicubic_img = cv2.resize(img,None, fx = .7, fy = .7, interpolation = cv2.INTER_CUBIC) 
cv2.imshow("Nearest Neighbour",near_img)
cv2.imshow("Billinear",bilinear_img)
cv2.imshow("Bicubic",bicubic_img)
cv2.waitKey()