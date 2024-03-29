from cv2 import cv2
from matplotlib import pyplot as plt
img=cv2.imread("Resources/Data/lena.png")
replicate=cv2.copyMakeBorder(img,100,10,10,10,cv2.BORDER_REPLICATE)
reflect=cv2.copyMakeBorder(img,100,10,10,10,cv2.BORDER_REFLECT)
wrap=cv2.copyMakeBorder(img,100,10,10,10,cv2.BORDER_WRAP)
val=[0,0,0]
constant=cv2.copyMakeBorder(img,100,10,10,10,cv2.BORDER_CONSTANT,value=val)
plt.figure(figsize=(11,8))
plt.subplot(231),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(232),plt.imshow(cv2.cvtColor(replicate,cv2.COLOR_BGR2RGB)),plt.title('Replicate')
plt.xticks([]),plt.yticks([])
plt.subplot(233),plt.imshow(cv2.cvtColor(reflect,cv2.COLOR_BGR2RGB)),plt.title('Reflect')
plt.xticks([]),plt.yticks([])
plt.subplot(234),plt.imshow(cv2.cvtColor(wrap,cv2.COLOR_BGR2RGB)),plt.title('Wrap')
plt.xticks([]),plt.yticks([])
plt.subplot(235),plt.imshow(cv2.cvtColor(constant,cv2.COLOR_BGR2RGB)),plt.title('Constant')
plt.xticks([]),plt.yticks([])
plt.show()