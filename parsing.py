# -*- coding: utf-8 -*-
"""parsing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n2zmYA7BV7GPu2Db7-8Q0S8jRK5j6M7l
"""

# use this code
# Parsing code: Fixing the data from https://github.com/rccorliss/tpc_alignment_data/OGP into a text file with each line representing a survey mark or stripes
# The first 4 lines are always survey marks, the rest is stripes. It is comma seperated x,y,z and z is always set to 0.

def parse_coordinates(petal_54):
    output_text = ''

    with open(petal_54, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if 'X Location' in line:
                x_coordinate = line.split()[4]
            elif 'Y Location' in line:
                y_coordinate = line.split()[4]
                output_text += f'{x_coordinate},{y_coordinate},0\n'

    return output_text

# Example usage
input_file_path = 'petal_54.txt'
output_text = parse_coordinates(input_file_path)

# Writing output to a file
with open('OGP_all_coord_54.txt', 'w') as file:
    file.write(output_text)
