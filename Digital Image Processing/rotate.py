from cv2 import cv2
img=cv2.imread("Resources/Data/lena.png")
(rows,cols)=img.shape[:2]
m=cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
rotate=cv2.warpAffine(img,m,(rows,cols))
cv2.imshow("Rotated Image",rotate)
cv2.waitKey()