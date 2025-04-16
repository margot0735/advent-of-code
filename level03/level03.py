## Advent of code day 3

# Objective : Compute the sum of the valid instructions (mul(X,Y)) 

import numpy as np
import os
import sys
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.tools import parse_file

#--- Main functions --- #

def level03_part1(input_path) -> int:
    """Compute the sum of the valid instructions (mul(X,Y))"""
    
    memory = parse_file(input_path)
    pattern_part1 = r"mul\((\d{1,3}),(\d{1,3})\)"

    valid_instructions = re.findall(pattern_part1, memory)

    sum_of_instructions = process_instructions(valid_instructions)

    return sum_of_instructions

def level03_part2(input_path) -> int:
    """Compute the sum of the valid instructions (mul(X,Y)) by considering do and don't instructions"""
    
    #init valid boolean to true 
    valid = True
    valid_instructions = []
    
    #parse part 2 pattern in txt file
    memory = parse_file(input_path)

    # add do and don't in the pattern
    pattern_part2 = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    
    for instruction in re.finditer(pattern_part2, memory):
        if instruction.group(0).startswith("mul("):                   # check if the full instruction starts with mul 
            x_str, y_str = instruction.group(2), instruction.group(3) # get instruction in the two first parentheses pairs
            if x_str is not None and y_str is not None and valid:
                valid_instructions.append((x_str, y_str))
        #update valid boolean regarding do and don't instructions
        elif instruction.group(0) == "do()":
            valid = True
        elif instruction.group(0) == "don't()":
            valid = False

    sum_of_instructions = process_instructions(valid_instructions)
    
    return sum_of_instructions


#--- Utility functions --- #

def process_instructions(instructions: list) -> int:
    """function for computing the sum of instructions"""

    result = 0
    for x_str, y_str in instructions:
        try:
            x = int(x_str)
            y = int(y_str)
            result += x * y
        except ValueError:
            print(f"invalid instruction: mul({x_str}, {y_str})")     
    return result


#--- Main call --- #

if __name__ == "__main__":
    file_path = "level03_input.txt"
    result_part1 = level03_part1(file_path)
    result_part2 = level03_part2(file_path)
    print("sum of instructions results for part 1:", result_part1) 
    print("sum of instructions results for part 2:", result_part2) 
