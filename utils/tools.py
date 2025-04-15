import numpy as np
import os
import sys

def process_input(file_path):

    # Verify if file exists
    if not os.path.isfile(file_path):
        print(f"error : file '{file_path}' not found")
        sys.exit(1)
    
    lists = np.loadtxt(file_path, delimiter=None , dtype=int)

    # Create 2 lists from the txt file
    list1 = lists[:, 0]  
    list2 = lists[:, 1] 

    return list1, list2
