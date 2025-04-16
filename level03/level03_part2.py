## Second part of advent of code day 3

# Objective : Compute the sum of the valid instructions (mul(X,Y)) considering the do and don't instructions

import os
import sys
import re

from utils.tools import verify_file

def main(input_path):

    verify_file(input_path)

    with open(input_path, 'r') as file:
        instructions = file.read()

    valid_instructions = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", instructions)
    
    result = 0
    for x_str, y_str in valid_instructions:
        x = int(x_str)
        y = int(y_str)
        result += x * y       
        
    return result


#--- Main call --- #

if __name__ == "__main__":
    file_path = "level03_input.txt"
    result = main(file_path)
    print("sum of instructions results:", result) 
