from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np
img=cv2.imread("Resources/Data/lena.png",)
rows,cols = img.shape[0],img.shape[1]
pts1 = np.float32([[56,56],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))
plt.figure(figsize=(11,6))
plt.subplot(121),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(cv2.cvtColor(dst,cv2.COLOR_BGR2RGB)),plt.title('Prespective')
plt.xticks([]),plt.yticks([])
plt.show()