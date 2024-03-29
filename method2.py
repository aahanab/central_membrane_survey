# -*- coding: utf-8 -*-
"""Method2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ll1Q3w36RDhu5HOKoxeZ7GI99Y_NPIjn
"""

import cv2
from google.colab.patches import cv2_imshow

def draw_bounding_boxes(image, points, lengths, widths):
    result = image.copy()
    for i, point in enumerate(points):
        x, y = point
        length, width = lengths[i], widths[i]
        start_x, start_y = int(x - length / 2), int(y - width / 2)
        end_x, end_y = int(x + length / 2), int(y + width / 2)
        cv2.rectangle(result, (start_x, start_y), (end_x, end_y), (0, 0, 255), 2)
    return result

# Load the image
image = cv2.imread("petal_54.jpg")

# Load the points from the text file
points = []
with open("output_transformed_pixelcoord_54.txt", "r") as file:
    lines = file.readlines()[4:]
    for i, line in enumerate(lines):
        x, y, z = map(float, line.strip().split())
        points.append((x, y))

# Define the lengths and widths of the stripes for the different size clusters
cluster1_lengths = [45]
cluster1_widths = [25]

cluster2_lengths = [65]
cluster2_widths = [35]

cluster3_lengths = [60]
cluster3_widths = [35]

# Determine the number of lines for each cluster
num_lines_cluster1 = 76
num_lines_cluster2 = 50

# Determine the number of points in each cluster
num_points_cluster1 = num_lines_cluster1
num_points_cluster2 = num_points_cluster1 + num_lines_cluster2

# Assign the lengths and widths to each point based on the cluster
lengths = []
widths = []
for i, point in enumerate(points):
    if i < num_points_cluster1:
        lengths += cluster1_lengths
        widths += cluster1_widths
    elif i < num_points_cluster2:
        lengths += cluster2_lengths
        widths += cluster2_widths
    else:
        lengths += cluster3_lengths
        widths += cluster3_widths

# Draw the bounding boxes
result = draw_bounding_boxes(image, points, lengths, widths)

# Display the result
cv2_imshow(result)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Method 2
# pixel_diffs = box_pixels - box_mean: relative brightness
# does not use threshold

import cv2
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt
import numpy as np

def calculate_pixel_histograms(image, points, lengths, widths):
    histograms = []
    for i, point in enumerate(points):
        x, y = point
        length, width = lengths[i], widths[i]
        start_x, start_y = int(x - length / 2), int(y - width / 2)
        end_x, end_y = int(x + length / 2), int(y + width / 2)

        # Extract the pixels within the box
        box_pixels = image[start_y:end_y, start_x:end_x]

        # Calculate the average pixel color
        box_mean = np.mean(box_pixels)

        # Calculate the difference between each pixel and the mean
        pixel_diffs = box_pixels - box_mean
        
        # Flatten the array of pixel differences
        pixel_diffs = pixel_diffs.flatten()

        # Add the pixel differences for this box to the list of histograms
        histograms.extend(pixel_diffs.tolist())
        
    return histograms

pixel_diffs = calculate_pixel_histograms(image, points, lengths, widths)

# Plot the histogram
plt.hist(pixel_diffs, bins=40,color=['red'], alpha=0.5)
plt.yscale('log')
plt.title("Relative Brightness Histogram: Method 2")
plt.xlabel("Pixel Brightness - Box Average")
plt.ylabel("Frequency" )
plt.show()