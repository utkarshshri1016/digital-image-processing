from cv2 import cv2
import numpy as np 
import argparse 
parser = argparse.ArgumentParser(description='Code for Changing the contrast and brightness of an image! tutorial.') 
parser.add_argument('--input', help='Path to input image.', default='Resources/Data/baboon.jpg') 
args = parser.parse_args() 
image = cv2.imread(cv2.samples.findFile(args.input)) 
if image is None: 
    print('Could not open or find the image: ', args.input) 
    exit(0) 
new_image = np.zeros(image.shape, image.dtype) 
alpha = 1.0 
beta = 0 
# Initialize values 
print(' Basic Linear Transforms ') 
print('-------------------------') 
try: 
    alpha = float(input('* Enter the alpha value [1.0-3.0]: ')) 
    beta = int(input('* Enter the beta value [0-100]: ')) 
except ValueError: 
    print('Error, not a number') 
for y in range(image.shape[0]): 
    for x in range(image.shape[1]): 
        for c in range(image.shape[2]): 
            new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255) 
cv2.imshow('Original Image', image) 
cv2.imshow('New Image', new_image) 
cv2.waitKey() 

 