from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np
img=cv2.imread("Resources/Data/brain.jpg")
kernel=np.ones((5,5),np.uint8)
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
plt.figure(figsize=(11,6))
plt.subplot(141),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(142),plt.imshow(opening,cmap='gray'),plt.title('Opening')
plt.xticks([]),plt.yticks([])
plt.subplot(143),plt.imshow(closing,cmap='gray'),plt.title('Closing')
plt.xticks([]),plt.yticks([])
plt.subplot(144),plt.imshow(gradient,cmap='gray'),plt.title('Gradient') #use alphabet here
plt.xticks([]),plt.yticks([])
plt.show()