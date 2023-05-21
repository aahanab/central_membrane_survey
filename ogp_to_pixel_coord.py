# -*- coding: utf-8 -*-
"""OGP_to_pixel_coord.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vGAAhjZjA09vXVll4eWVk8ZYzqXXl9Kz
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from math import sqrt
import math

def read_coordinates(file_path):
    # Initialize an empty list to store the coordinates
    coordinates = []
    
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read each line of the file
        for line in file:
            # Skip empty lines or lines that do not contain three values 
            if not line.strip() or len(line.strip().split(',')) != 3:
                continue
            # Split the line by whitespace to get the x, y, and z coordinates
            x, y, z = map(float, line.strip().split(','))
            
            # Append the coordinates to the list
            coordinates.append([x, y, z])
            
    # Return the coordinates as a NumPy matrix
    return np.matrix(coordinates)

# Read the coordinates of B from a text file
B = read_coordinates('OGP_survey_marks.txt')

# Read the coordinates of A from a text file
A = read_coordinates('pixel_survey_marks.txt')


scaling = True

# Implements Kabsch algorithm  
# Input:
#     Nominal  A Nx3 matrix of points
#     Measured B Nx3 matrix of points
# Returns s,R,t
# s = scale B to A
# R = 3x3 rotation matrix (B to A)
# t = 3x1 translation vector (B to A)

def transform_3D(A, B, scale):
    assert len(A) == len(B)

    N = A.shape[0];  # total points

    centroid_A = np.mean(A, axis=0)
    centroid_B = np.mean(B, axis=0)

    # center the points
    AA = A - np.tile(centroid_A, (N, 1))
    BB = B - np.tile(centroid_B, (N, 1))

    # dot is matrix multiplication for array
    if scale:
        H = np.transpose(BB) * AA / N
    else:
        H = np.transpose(BB) * AA

    U, S, Vt = np.linalg.svd(H)

    R = Vt.T * U.T

    # special reflection case
    if np.linalg.det(R) < 0:
        #print ("Reflection detected")
        Vt[2, :] *= -1 
        R = Vt.T * U.T

    if scale:
        varA = np.var(A, axis=0).sum()
        c = 1 / (1 / varA * np.sum(S))  # scale factor
        t = -R * (centroid_B.T * c) + centroid_A.T
    else:
        c = 1
        t = -R * centroid_B.T + centroid_A.T

    return c, R, t

################################################################################################################
################################################################################################################

# Test

n = B.shape[0]

# recover the transformation

s, ret_R, ret_t = transform_3D(A, B, scaling)

# Read the coordinates of OGP_2.txt which has all the coordinates. It has x,y,z comma seperated and z is set to 0. 
#If it is an integer, put a .0 after it since it only reads float.

coordinates = read_coordinates('OGP_all_coord.txt')

# Add a fourth row of ones to the coordinates to make them homogeneous

homogeneous_coordinates = np.concatenate((coordinates, np.ones((coordinates.shape[0], 1))), axis=1)

# Create the transformation matrix

transformation_matrix = np.concatenate((s * ret_R, ret_t), axis=1)

# Transform the coordinates, have to transpose for multiplication since matrices are two different sizes

transformed_coordinates = homogeneous_coordinates @ transformation_matrix.T

# Remove the fourth row (which was added to make the coordinates homogeneous)

transformed_coordinates = transformed_coordinates[:, :3]

# The transformed coordinates are now stored in the transformed_coordinates variable

#convert to 4x4 transform
match_target = np.zeros((4,4))
match_target[:3,:3] = ret_R
match_target[0,3] = ret_t[0]
match_target[1,3] = ret_t[1]
match_target[2,3] = ret_t[2]
match_target[3,3] = 1

############################################################################################################
############################################################################################################

# Open the file in write mode and output the information in text files. 
# One text file is output1 which only stores the transformation info
# Second tect file is output2 which stores all the transformed pixel coordiniates to plot on the image later. 


with open('output_transforms.txt', 'w') as f:
  # Write the scale factor
  f.write(f"Scale factor: {s:>10.4f}\n")

  # Write the rotation matrix
  f.write("Rotation matrix:\n")
  for row in np.array(ret_R):
    f.write(" ".join([f"{element:>10.4f}" for element in row]) + "\n")

  # Write the translation vector
  f.write("Translation vector:\n")
  for row in np.array(ret_t):
    f.write(" ".join([f"{element:>10.4f}" for element in row]) + "\n")

  # Write the homogenous transformation matrix
  f.write("Homogenous transformation matrix:\n")
  for row in np.array(match_target):
    f.write(" ".join([f"{element:>10.4f}" for element in row]) + "\n")
  
  # Write the homogenous transformation matrix
  f.write("Pixel coord:\n")
  for row in np.array(A):
    f.write(" ".join([f"{element:>10.4f}" for element in row]) + "\n")

  # Write the homogenous transformation matrix
  f.write("OGB coord:\n")
  for row in np.array(B):
    f.write(" ".join([f"{element:>10.4f}" for element in row]) + "\n")
    
  # Write the homogenous transformation matrix
  f.write("Calculated pixel coord:\n")
  for row in np.array(transformed_coordinates):
    f.write(" ".join([f"{element:>10.4f}" for element in row]) + "\n")
    
############################################################################################################

with open('output_transformed_pixelcoord.txt', 'w') as f:
  
  for row in np.array(transformed_coordinates):
    f.write(" ".join([f"{element:>10.4f}" for element in row]) + "\n")
    
    
#############################################################################################################
#############################################################################################################

print("Transformation information:")
print("")
      
print ("Rotation")
print (ret_R)
print ("")

print ("Translation")
print (ret_t)
print ("")

print ("Scale")
print (s)
print ("")

print ("Homogeneous Transform Matrix")
print (match_target)
print ("")





