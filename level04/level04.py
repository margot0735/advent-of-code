## Advent of code day 4

# Objective : 

import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.tools import parse_file

#--- Main functions --- #

def level04_part1(input_path) ->int:
    word_search = parse_file(input_path)

    word_count = 0
    return word_count

def level04_part2(input_path) ->int:
    word_count = 0
    return word_count
    

#--- Utility functions --- #



#--- Main call --- #

if __name__ == "__main__":
    file_path = "level04_input.txt"
    result_part1 = level04_part1(file_path)
    result_part2 = level04_part2(file_path)
    print("sum of instructions results for part 1:", result_part1) 
    print("sum of instructions results for part 2:", result_part2) 

