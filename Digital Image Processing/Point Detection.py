from cv2 import cv2
import numpy as np
img=cv2.imread("Resources/Data/lena.png",0)
m, n=img.shape
l=img.max()
img_neg=l-img
cv2.imshow("Negative Lena",img_neg)
t=150
img_thresh=np.zeros((m,n),dtype=np.uint8)
for i in range (m):
    for j in range(n):
        if img[i,j]<t:
            img_thresh[i,j]=0
        else:
            img_thresh[i,j]=255
cv2.imshow("Lena Thresh",img_thresh)
cv2.waitKey()