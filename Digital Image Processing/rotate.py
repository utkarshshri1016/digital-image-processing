    from cv2 import cv2
img=cv2.imread("Resources/Data/lena.png")
(rows,cols)=img.shape[:2]
m=cv2.getRotationMatrix2D((cols/2,rows/2),30,1)
rotate=cv2.warpAffine(img,m,(rows,cols))
rotate1=cv2.warpAffine(rotate,m,(rows,cols))
rotate2=cv2.warpAffine(rotate,m,(rows,cols))
cv2.imshow("Rotated Image",rotate2)
cv2.waitKey()