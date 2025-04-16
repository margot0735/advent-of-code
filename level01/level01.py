## Advent of code day 1

# Objective : Compute the total distance between pairs from the 2 lists given as input of the problem 

import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.tools import process_list

def level01_part1(input_path):
    # Load file
    list1, list2 = process_list(input_path)

    # Pair numbers
    list1_ranked = np.sort(list1)
    list2_ranked = np.sort(list2)

    #Compute distance for each pair
    pair_difference = np.abs(list1_ranked-list2_ranked)
    total_distance = np.sum(pair_difference)

    return total_distance

def level01_part2(input_path):
    # Load file
    list1, list2 = process_list(input_path)

    # Initialize similarity score array 
    similarity_score=[]

    # Compute similarity score for each value of list1
    for i in range(len(list1)):
        occurence = np.count_nonzero(np.array(list2) == list1[i])
        similarity_score.append(list1[i] * occurence)

    # Compute total similarity score
    total_similarity = np.sum(similarity_score)

    return total_similarity


# --- Main call --- #

if __name__ == "__main__":
    file_path = "level01_input.txt"
    result_part1 = level01_part1(file_path)
    result_part2 = level01_part2(file_path)
    print("total distance:", result_part1) 
    print("total similarity score:", result_part2) 
