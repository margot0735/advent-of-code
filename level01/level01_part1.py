## First part of advent of code day 1
# Objective : Compute the total distance between pairs from the 2 lists given as input of the problem 

import numpy as np
import os
import sys

# Load file
file_path = "level01_part1_input.txt"

# Verify if file exists
if not os.path.isfile(file_path):
    print(f"error : file '{file_path}' not found")
    sys.exit(1)

lists = np.loadtxt(file_path, delimiter=None , dtype=int)

# Create 2 lists
list1 = lists[:, 0]  
list2 = lists[:, 1]

if len(list1) != len(list2):
    print("Error : the two lists don't have the same size")
    sys.exit(1)

# Pair numbers
list1_ranked = np.sort(list1)
list2_ranked = np.sort(list2)

# Print results
# print("Column 1:", list1)
# print("Column 2:", list2)
# print("Column 1 ranked:", list1_ranked)
# print("Column 2 ranked:", list2_ranked)

#Compute distance for each pair
pair_difference = np.abs(list1_ranked-list2_ranked)
total_distance = np.sum(pair_difference)

# Print the total distance
print("total distance:", total_distance)
