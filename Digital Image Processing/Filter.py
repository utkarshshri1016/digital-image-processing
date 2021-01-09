from cv2 import cv2
from matplotlib import pyplot as plt
img1=cv2.imread("Resources/Data/brain.jpg")
img=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
figure_size=7
new_img=cv2.blur(img,(figure_size,figure_size))
plt.figure(figsize=(11,6))
plt.subplot(121),plt.imshow(cv2.cvtColor(img,cv2.COLOR_HSV2RGB)),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(cv2.cvtColor(new_img,cv2.COLOR_HSV2RGB)),plt.title('Mean Filter')
plt.xticks([]),plt.yticks([])
plt.show()