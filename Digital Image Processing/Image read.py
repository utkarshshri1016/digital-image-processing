from cv2 import cv2
img=cv2.imread("C:/Users/utkar/Desktop/Digital Image Processing/image.jpeg")
print(img)
cv2.imshow('image', img) 
cv2.waitKey()