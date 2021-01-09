from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np
img=cv2.imread("Resources/Data/lena.png")
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
f=np.fft.fft2(img_gray)
fshift=np.fft.fftshift(f)
magnitude_spectrum=20*np.log(np.abs(fshift))
plt.figure(figsize=(11,6))
plt.subplot(121),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum,cmap='gray'),plt.title('Magnitude Spectrum')
plt.xticks([]),plt.yticks([])
plt.show()