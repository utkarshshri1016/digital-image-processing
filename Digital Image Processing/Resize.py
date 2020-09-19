from cv2 import cv2
img=cv2.imread("Resources/Data/lena.png")
(height,width)=img.shape[:2]
res_img=cv2.resize(img,(int(width/2),int(height/2)),interpolation=cv2.INTER_CUBIC)
cv2.imshow("resize",res_img)
cv2.waitKey()
zoom=cv2.resize(img,None,fx=2.0, fy=2.5,interpolation=cv2.INTER_CUBIC)
cv2.imshow("zoomed",zoom)
cv2.waitKey()
