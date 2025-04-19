# file : level02.py
# description : Advent of code day 1## Advent of code day 2

# Objective : 

import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.tools import verify_file

# --- Main function --- #

def level02_part1(input_path) -> int:
    return count_safe_reports(input_path, tolerate=False)

def level02_part2(input_path) -> int:
    return count_safe_reports(input_path, tolerate=True)


# --- Utility functions --- #

def is_increasing(report) ->bool:      
    return np.all(report[1:] > report[:-1])

def is_decreasing(report) ->bool:      
    return np.all(report[1:] < report[:-1])

def has_valid_level_difference(report) ->bool:    
    level_difference = np.abs(report[1:] - report[:-1])
    return np.all((level_difference >= 1) & (level_difference <= 3))  

def is_safe(report) ->bool:
    """Check if a report is safe based on increasing/decreasing and level difference."""
    return (is_increasing(report) or is_decreasing(report)) and has_valid_level_difference(report)

def count_tolerated_pattern(report) ->int:
    pattern = 0
    for level in range(len(report)):
        reduced_report = np.delete(report, level) #remove one level at a time
        #compute working number of patterns
        if is_safe(reduced_report):
            pattern += 1
    return pattern

def count_safe_reports(input_path, tolerate=False) ->int:
    reports_list = process_arrays(input_path)
    safe_report = 0

    for report in reports_list:
        if is_safe(report):
            safe_report += 1
        elif tolerate and count_tolerated_pattern(report) >= 1:
            safe_report += 1

    return safe_report

def process_arrays(file_path):
    """
    Function for creating a list of arrays of shape (1, y) from a txt file.
    Each line in the file is expected to contain space-separated integers.
    """
    verify_file(file_path)

    arrays_list = []
    # Create list of arrays 
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():                        # Ignore blank lines
                array = np.array(list(map(int, line.strip().split())))   # Convert line to array of int
                arrays_list.append(array)
    
    return arrays_list


# --- Main call --- #

if __name__ == "__main__":
    file_path = "level02_input.txt"
    result_part1 = level02_part1(file_path)
    result_part2 = level02_part2(file_path)
    print("initial safe report count:", result_part1) 
    print("total safe report count:", result_part2) 

