from cv2 import cv2
from matplotlib import pyplot as plt
import numpy as np
img=cv2.imread("Resources/Data/103204.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,75,150)
lines=cv2.HoughLinesP(edges,1,np.pi/180,30,maxLineGap=250)
for line in lines:
    x1,y1,x2,y2=line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,128),1)
cv2.imshow("Lines Edges",edges)
cv2.imshow("Lines Detected",img)
cv2.waitKey()    