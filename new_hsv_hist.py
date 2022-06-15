import cv2 as cv
import numpy as np
from numpy.lib.histograms import histogram
import matplotlib.pyplot as plt
import matplotlib.colors as colors

image_original = cv.imread('img3_3.jpg')
image_hsv = cv.cvtColor(image_original, cv.COLOR_BGR2HSV)

rgbImage = cv.imread('img3_3.jpg')
#hsvImage = rgb2hsv(rgbImage)
array=np.asarray(rgbImage)
arr=(array.astype(float))/255.0
hsvImage = cv.cvtColor(image_original, cv.COLOR_BGR2HSV)
hsvImage = colors.rgb_to_hsv(arr[...,:3])
hImage = hsvImage[...,0]
sImage = hsvImage[...,1]
vImage = hsvImage[...,2]

plt.subplot(2,2,1)
hHist = plt.hist(hImage*180,bins=360,range=(0.0,180.0),histtype='stepfilled')
plt.grid()
plt.title("Hue Histogram")

plt.subplot(2,2,2)
sHist = plt.hist(sImage)
plt.grid()
plt.title("Saturation Histogram")

plt.subplot(2,2,3)
vHist = plt.hist(vImage)
plt.grid()
#plt.title("Value Histogram")
#plt.subplot(2,2,4)

#imshow(rgbImage)


#########################################################################################
#hue histogram for gold 
image_original = cv.imread('img3_3.jpg')
image_hsv = cv.cvtColor(image_original, cv.COLOR_BGR2HSV)

gold_hist=plt.hist(x=image_hsv.ravel(), bins=360, range=[0, 180], color='blue')
plt.title("Histogram Showing pixel # and hue", color='blue')
plt.ylabel("Number Of Pixels", color="blue")
plt.xlabel("Pixel Hue", color="blue")
plt.show()

#############################################################################################
#hue histogram for the stripe
image_original = cv.imread('img3_2.jpg')
image_hsv = cv.cvtColor(image_original, cv.COLOR_BGR2HSV)

wstripe_hist=plt.hist(x=image_hsv.ravel(), bins=360, range=[0, 180], color='red')
plt.title("Histogram Showing pixel # and hue", color='red')
plt.ylabel("Number Of Pixels", color="red")
plt.xlabel("Pixel Hue", color="red")
plt.show()
