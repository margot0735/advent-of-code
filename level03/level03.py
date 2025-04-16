## Advent of code day 3

# Objective : Compute the sum of the valid instructions (mul(X,Y)) 

import os
import sys
import re

from utils.tools import verify_file

#--- Main functions --- #

def part1(input_path) -> int:
    """Compute the sum of the valid instructions (mul(X,Y))"""
    
    memory = parse_instructions(input_path)
    pattern_part1 = r"mul\((\d{1,3}),(\d{1,3})\)"

    valid_instructions = re.findall(pattern_part1, memory)

    sum_of_instructions = process_instructions(valid_instructions)

    return sum_of_instructions

def part2(input_path) -> int:
    """Compute the sum of the valid instructions (mul(X,Y)) by considering do and don't instructions"""
    
    #init
    valid = True
    valid_instructions = []
    
    #parse part 2 pattern in txt file
    memory = parse_instructions(input_path)

    pattern_part2 = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    
    for match in re.finditer(pattern_part2, memory):
        if match.group(1):  # If it's a mul instruction
            x, y = match.group(2), match.group(3)
            valid_instructions.append((x, y, valid))
        elif match.group(0) == "do()":
            valid = True
        elif match.group(0) == "don't()":
            valid = False
    
    # Process instructions if instruction is valid
    sum_of_instructions = process_instructions([x_y[0:2] for x_y in valid_instructions if x_y[2]])
    
    return sum_of_instructions


#--- Utility functions --- #

def parse_instructions(input_path) -> list:
    """function for reading txt file and finding the requested pattern"""

    verify_file(input_path)

    with open(input_path, 'r') as file:
        memory = file.read()

    return memory

def process_instructions(instructions: list) -> int:
    
    result = 0
    for x_str, y_str in instructions:
        x = int(x_str)
        y = int(y_str)
        result += x * y       
    return result


#--- Main call --- #

if __name__ == "__main__":
    file_path = "level03_input.txt"
    result_part1 = part1(file_path)
    result_part2 = part2(file_path)
    print("sum of instructions results for part 1:", result_part1) 
    print("sum of instructions results for part 2:", result_part2) 
