## Second part of advent code day 1

# Objective : Compute the similarity score between the 2 lists given as input of the problem 

import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.tools import process_lists

def main(input_path):
    # Load file
    list1, list2 = process_lists(input_path)

    # Initialize similarity score array 
    similarity_score=[]

    # Compute similarity score for each value of list1
    for i in range(len(list1)):
        occurence = np.count_nonzero(np.array(list2) == list1[i])
        similarity_score.append(list1[i] * occurence)

    # Compute total similarity score
    total_similarity = np.sum(similarity_score)

    return total_similarity


if __name__ == "__main__":
    file_path = "level01_input.txt"
    result = main(file_path)
    print("total similarity score:", result)