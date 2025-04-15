## First part of advent of code day 3

# Objective : Compute the sum of the valid instructions (mul(X,Y)) results 

import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def main(input_path):

    # Verify if file exists
    if not os.path.isfile(input_path):
        print(f"error : reports file '{input_path}' not found")
        sys.exit(1)

    with open(input_path, 'r') as file:
        instructions = file.read()

    valid_instructions = []

    character = 0
    while character < len(instructions):
        
        instruction_start = instructions.find("mul(",character)
        if instruction_start == -1:
            break

        instruction_end = instructions.find(")",instruction_start)
        if instruction_end == -1:
            break
        
        number_sequence = instructions[instruction_start+4:instruction_end]   
        
        if ',' in number_sequence:
            x_string, y_string = number_sequence.split(',', 1)
            X = try_convert(x_string)
            Y = try_convert(y_string)
            print(X,Y)

            if isinstance(X, (int, float)) and isinstance(Y, (int, float)):
                valid_instructions.append(X * Y)
            # else:
            #   print(f"This is not a valid instruction")

        character = instruction_start + 1       

    return sum(valid_instructions)


def try_convert(value):
    # Try converting in int or float
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value.strip()

#--- Main call --- #

if __name__ == "__main__":
    file_path = "level03_input.txt"
    result = main(file_path)
    print("sum of instructions results:", result) 
