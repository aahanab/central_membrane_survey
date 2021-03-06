import scipy
from scipy import ndimage
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from scipy import misc
import scipy.misc
import imageio

img = imageio.imread('img3_2.jpg')
array=np.asarray(img)
arr=(array.astype(float))/255.0
img_hsv = colors.rgb_to_hsv(arr[...,:3])

lu1=img_hsv[...,0].ravel()  #.flatten()
plt.subplot(1,3,1)
plt.hist(lu1*180,bins=360,range=(0.0,180.0),histtype='stepfilled', color='r', label='Hue')
plt.grid()
plt.title("Hue")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()

lu2=img_hsv[...,1].ravel()
plt.subplot(1,3,2)                  
plt.hist(lu2*255,bins=255,range=(0.0,255.0),histtype='stepfilled', color='g', label='Saturation')
plt.grid()
plt.title("Saturation")   
plt.xlabel("Value")    
plt.ylabel("Frequency")
plt.legend()

lu3=img_hsv[...,2].ravel()
plt.subplot(1,3,3)                  
plt.hist(lu3*255,bins=256,range=(0.0,255.0),histtype='stepfilled', color='b', label='Intesity')
plt.grid()
plt.title("Intensity")   
plt.xlabel("Value")    
plt.ylabel("Frequency")
plt.legend()
plt.show()
