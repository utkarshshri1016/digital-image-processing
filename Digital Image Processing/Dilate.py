from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np
img=cv2.imread("Resources/Data/e.png")
kernel=np.ones((5,5),np.uint8)
erosion1=cv2.dilate(img,kernel,iterations=1)
erosion5=cv2.dilate(img,kernel,iterations=5)
plt.figure(figsize=(11,6))
plt.subplot(131),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(132),plt.imshow(erosion1,cmap='gray'),plt.title('In 1 Iteration')
plt.xticks([]),plt.yticks([])
plt.subplot(133),plt.imshow(erosion5,cmap='gray'),plt.title('In 5 Iterations')
plt.xticks([]),plt.yticks([])
plt.show()