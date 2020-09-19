from cv2 import cv2
import numpy as np
img=cv2.imread("Resources/Data/lena.png")
(height,width)=img.shape[:2]
cv2.imshow("Original",img)
translation_matrix=np.float32([[1,0,70],[0,1,110]])
translation=cv2.warpAffine(img,translation_matrix,(height,width))
cv2.imshow("Translated",translation)
cv2.waitKey()