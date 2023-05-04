# -*- coding: utf-8 -*-
"""finding_coord.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1beLMJ5446bx6To6PnHtzKZJr2Sv5gNo-
"""
#Please run the following dependencies before running the main code.
# If you hover over any part of the image and click on it, it prints out the coordinates as pixel coordinates 
# You may chpoose a more specifi location (like the center of the survey mark) by click on a surrounding area, and it will zoom in. 
# Then you can go ahead and click on it and it prints out the pixel coord.

#####################################################
#Dependencies
!pip install ipympl

from google.colab import output
output.enable_custom_widget_manager()

# Commented out IPython magic to ensure Python compatibility.
 %matplotlib ipympl

from google.colab import output
output.enable_custom_widget_manager()

# Main code is below
####################################################
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
%matplotlib ipympl
from google.colab.patches import cv2_imshow
import cv2

f1 = 'flipped_mono.jpg' #Please use the respective petal images. 

img = mpimg.imread(f1)

fig,ax = plt.subplots()
img1 = ax.imshow(img)

def onclick(event):
    ix, iy = event.xdata, event.ydata
    print(ix, iy)

cid = fig.canvas.mpl_connect('button_press_event', onclick)

