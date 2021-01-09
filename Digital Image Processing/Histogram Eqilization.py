import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("Resources/Data/lena.png",0)
equ = cv2.equalizeHist(img)
plt.figure(figsize=(11,6))
plt.subplot(121),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(equ,cmap='gray'),plt.title('Histogram Equalized')
plt.xticks([]),plt.yticks([])
plt.show()