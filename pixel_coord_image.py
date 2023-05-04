# -*- coding: utf-8 -*-
"""pixel_coord_image.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ox5sq5yGSXslPw1KhKH7vimaPLeY1cQC
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
from matplotlib.pyplot import figure


# Read the input image
image = cv2.imread("flipped_mono.jpg")

# Read the points from the text file
points = []
with open('output2.txt', 'r') as file:
    # Read each line of the file
    for line in file:
        # Split the line by commas to get the x, y, and z coordinates
        x, y, z = map(float, line.strip().split())
        # Append the x and y coordinates to the list
        points.append([x, y])

# Convert the points to a NumPy array
points = np.array(points)

# Get the dimensions of the input image
height, width, _ = image.shape

# Set the figure size to match the dimensions of the input image
figure(figsize=(width / 100, height / 100), dpi=100)

# Display the input image and the points
plt.imshow(image)
plot = plt.scatter(points[:, 0], points[:, 1], marker="o", color="red", s=1)

# Save the plot as an image
plt.savefig("plot_image.png", dpi=100, bbox_inches='tight', pad_inches=0)

