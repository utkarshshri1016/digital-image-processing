from cv2 import cv2
from matplotlib import pyplot as plt
img=cv2.imread("Resources/Data/lena.png")
wrap=cv2.copyMakeBorder(img,100,10,10,10,cv2.BORDER_WRAP)
plt.figure(figsize=(11,6))
plt.subplot(121),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(cv2.cvtColor(wrap,cv2.COLOR_BGR2RGB)),plt.title('Wrap')
plt.xticks([]),plt.yticks([])
plt.show()