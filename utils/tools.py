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
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():            # Ignore blank lines
                # Convert line to array of int
                report_array = np.array(list(map(int, line.strip().split())))
                reports_list.append(report_array)
    
    return reports_list

def try_convert(value):
    # Try converting in int or float
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value.strip()

def process_instructions(file_path):

    # Verify if file exists
    if not os.path.isfile(file_path):
        print(f"error : reports file '{file_path}' not found")
        sys.exit(1)

    with open(file_path, 'r') as file:
        content = file.read()

    instructions = []

    character = 0
    while character < len(content):
        if ((content[character:character+4] == 'mul(') and (content[character+8] == ')')):

            X = try_convert(content[character+5])
            Y = try_convert(content[character+7])

            if isinstance(x, (int, float)) and isinstance(y, (int, float)):
                instructions.append(X * Y)
            else:
                print(f"This is not a valid instruction")
        else:
            character+= 1

    return instructions

