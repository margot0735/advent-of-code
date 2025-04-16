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

def level02_part1(input_path) -> int:
    """function for computing the number of initial safe reports based on the 3 conditions"""
    list_of_reports = process_reports(input_path)
    safe_reports_count  = 0

    for report in list_of_reports:
        if ((verify_increasing(report) or verify_decreasing(report)) and verify_level_difference(report)):
            safe_reports_count  +=1

    return safe_reports_count 

def level02_part2(input_path) -> int:
    """function for computing the number of new safe reports based on the condition tolerated"""
    safe_reports_count  = 0
    list_of_reports = process_reports(input_path)
    new_safe_reports_count = 0

    for report in list_of_reports:
        if ((verify_increasing(report) or verify_decreasing(report)) and verify_level_difference(report)):
            safe_reports_count  +=1
        # for each unsafe reports
        # verify if at least one new pattern can be tolerated when removing one level at a time
        elif(verify_tolerated_pattern(report)>=1):
            new_safe_reports_count  +=1

    return safe_reports_count + new_safe_reports_count

# --- Reports verifications function --- #

def verify_increasing(report):      
    return np.all(report[1:] > report[:-1])


def verify_decreasing(report):      
    return np.all(report[1:] < report[:-1])


def verify_level_difference(report):    
    level_difference = np.abs(report[1:] - report[:-1])
    return np.all((level_difference >= 1) & (level_difference <= 3))  

def verify_tolerated_pattern(report):
    pattern = 0
    for level in range(len(report)):
        reduced_report = np.delete(report, level) #remove one level at a time
        #compute working number of patterns
        if ((verify_increasing(reduced_report) or verify_decreasing(reduced_report)) and verify_level_difference(reduced_report)):
            pattern += 1
    return pattern


# --- Main call --- #

if __name__ == "__main__":
    file_path = "level02_input.txt"
    result_part1 = part1(file_path)
    result_part2 = part2(file_path)
    print("initial safe report count:", result_part1) 
    print("total safe report count:", result_part2) 

