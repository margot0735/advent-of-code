## First part of advent of code day 2

# Objective : Compute the number of safe report(s) in the report list given as input of the problem
# A report only counts as safe if both of the following are true:
# - The levels are either all increasing or all decreasing.
# - Any two adjacent levels differ by at least one and at most three.

import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.tools import process_reports

def main(input_path):
    list_of_reports = process_reports(file_path)
    safe_reports_count  = 0

    for report in list_of_reports:
        if ((verify_increasing(report) or verify_decreasing(report)) and verify_level_difference(report)):
            safe_reports_count  +=1

    return safe_reports_count 

# --- Reports verifications function --- #

def verify_increasing(report):      
    return np.all(report[1:] > report[:-1])


def verify_decreasing(report):      
    return np.all(report[1:] < report[:-1])


def verify_level_difference(report):    
    level_difference = np.abs(report[1:] - report[:-1])
    return np.all((level_difference >= 1) & (level_difference <= 3))  


# --- Main call --- #

if __name__ == "__main__":
    file_path = "level02_input.txt"
    result = main(file_path)
    print("safe report count:", result) 

