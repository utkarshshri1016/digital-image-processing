from cv2 import cv2
import numpy as np
img=cv2.imread("Resources/Data/lena.png")
rows,cols=img.shape[0],img.shape[1]
m=np.float32([[1,0,100],[0,1,50]])
dst=cv2.warpAffine(img,m,(rows,cols))
cv2.imshow("Translated Image",dst)
cv2.waitKey()