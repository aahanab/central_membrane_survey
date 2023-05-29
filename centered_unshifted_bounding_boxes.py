# -*- coding: utf-8 -*-
"""centered_unshifted_bounding_boxes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qb__1uFVksDUT8R7K6u74eBl9pOJtX34
"""

# Code to produce bounding boxes where length and width is equi-distance from the points
# It divides the petal into three different 'clusters'since stripes are of different lengths.
# The clusters have a fixed lenth and width that is hardcoded. It seemes to work with all petals.
# This code plots the bounding boxes centered around without any shift with the transformed pixel coordinates. 

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
image = cv2.imread("flipped_mono.jpg")

# Load the points from the text file
points = []
with open("output2.txt", "r") as file:
    lines = file.readlines()
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