from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np
img=cv2.imread("Resources/Data/lena.png")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
f=np.fft.fft2(img_gray)
fshift=np.fft.fftshift(f)
f_ishift=np.fft.ifftshift(fshift)
img_back=np.fft.ifft2(f_ishift)
img_back=np.abs(img_back)
plt.figure(figsize=(11,6))
plt.subplot(131),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(132),plt.imshow(img_back,cmap='gray'),plt.title('Image after HPF')
plt.xticks([]),plt.yticks([])
plt.subplot(133),plt.imshow(img_back),plt.title('Result in JET')
plt.xticks([]),plt.yticks([])
plt.show()