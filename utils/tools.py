import numpy as np
import os
import sys

def verify_file(file_path):
    """function for verifying if txt file exists"""
    if not os.path.isfile(file_path):
        print(f"error : lists file '{file_path}' not found")
        sys.exit(1)

def parse_file(input_path) -> list:
    """function for reading txt file and returning the text in a list"""

    verify_file(input_path)

    with open(input_path, 'r') as file:
        input_list = file.read()

    return input_list

def process_list(file_path):
    """function for creating 2 arrays of shape (x,1) from a txt file"""
    verify_file(file_path)
    
    lists = np.loadtxt(file_path, delimiter=None , dtype=int)

    # Create 2 lists from the txt file
    list1 = lists[:, 0]  
    list2 = lists[:, 1] 

    return list1, list2

def process_arrays(file_path):
    """function for creating a list of n arrays of shape (1,y) from a txt file"""

    verify_file(file_path)

    arrays_list = []
    # Create list of arrays 
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():                        # Ignore blank lines
                arrays_list = np.array(list(map(int, line.strip().split())))   # Convert line to array of int
                arrays_list.append(arrays_list)
    
    return arrays_list
