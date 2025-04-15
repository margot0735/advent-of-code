import numpy as np
import os
import sys

def process_lists(file_path):

    # Verify if file exists
    if not os.path.isfile(file_path):
        print(f"error : lists file '{file_path}' not found")
        sys.exit(1)
    
    lists = np.loadtxt(file_path, delimiter=None , dtype=int)

    # Create 2 lists from the txt file
    list1 = lists[:, 0]  
    list2 = lists[:, 1] 

    return list1, list2

def process_reports(file_path):

    # Verify if file exists
    if not os.path.isfile(file_path):
        print(f"error : reports file '{file_path}' not found")
        sys.exit(1)
    
    reports_list = []

    # Create list of arrays 
    with open(file_path, 'r') as f:
        for line in f:
            if line.strip():            # Ignore blank lines
                # Convert line to array of int
                report_array = np.array(list(map(int, line.strip().split())))
                reports_list.append(report_array)
    
    return reports_list