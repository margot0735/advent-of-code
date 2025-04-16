## Advent of code day 4

# Objective : 

import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.tools import parse_file

#--- Main functions --- #
def read_input(input_path):
    with open(input_path, 'r') as file:
        input_list = file.read().strip().splitlines()
    return [list(row.strip()) for row in input_list]

def level04_part1(input_path) -> int:  
    word = "XMAS"
    word_length = len(word)
    word_search = read_input(input_path)
    rows = len(word_search)
    cols = len(word_search[0])
    word_count = 0

    def matches(i, j, dx, dy):
        for k in range(word_length):
            x = i + k*dx
            y = j + k*dy
            if not (0 <= x < rows and 0 <= y < cols) or (word_search[x][y]!=word[k]):
                return False
        return True

    for i in range(rows):
        for j in range(cols):
            directions = [(1, 0),(-1, 0),(0, 1),(0, -1),(1, 1),(-1, -1),(-1, 1),(1, -1)]
            for dx, dy in directions:
                if matches(i, j, dx, dy):
                    word_count += 1

    return word_count


# #--- Utility functions --- #




def level04_part2(input_path) -> int:
    word_count = 0
    return word_count


#--- Main call --- #
def main():
    file_path = "level04_input.txt"
    result_part1 = level04_part1(file_path)
    #result_part2 = level04_part2(file_path)
    print("number of word found:", result_part1) 
    #print("":", result_part2)

if __name__ == "__main__":
    main()


