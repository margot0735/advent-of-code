## First part of advent of code day 1

# Objective : Compute the total distance between pairs from the 2 lists given as input of the problem 

import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.tools import process_list

def main(input_path):
    # Load file
    list1, list2 = process_list(input_path)

    # Pair numbers
    list1_ranked = np.sort(list1)
    list2_ranked = np.sort(list2)

    #Compute distance for each pair
    pair_difference = np.abs(list1_ranked-list2_ranked)
    total_distance = np.sum(pair_difference)

    return total_distance


if __name__ == "__main__":
    file_path = "level01_input.txt"
    result = main(file_path)
    print("total distance:", result)
