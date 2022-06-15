import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
image_original = cv.imread('grayscale.bmp')

#gold does not have "blue" in it so that is why we defined only upper and lower blue

# Convert BGR to HSV
image_hsv = cv.cvtColor(image_original, cv.COLOR_BGR2HSV)

# define range of blue color in HSV (Hue, stauration, brightness) -> keep saturation low 
lower_blue = np.array([80,10,50]) # original (110,10,50)
upper_blue = np.array([160,255,255]) # original (175,255,255)
 
# Threshold the HSV image to get only blue colors
image_mask = cv.inRange(image_hsv, lower_blue, upper_blue)

#plt.imshow(image_original)
#plt.imshow(image_hsv)
plt.imshow(image_mask)
# will outline the rectangles
#plt.imshow(cv.Laplacian(image_mask, cv.CV_8U))

