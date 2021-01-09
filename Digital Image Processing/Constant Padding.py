from cv2 import cv2
from matplotlib import pyplot as plt
img=cv2.imread("Resources/Data/lena.png")
val=[0,0,0]
constant=cv2.copyMakeBorder(img,100,10,10,10,cv2.BORDER_CONSTANT,value=val)
plt.figure(figsize=(11,6))
plt.subplot(121),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(cv2.cvtColor(constant,cv2.COLOR_BGR2RGB)),plt.title('Constant')
plt.xticks([]),plt.yticks([])
plt.show()