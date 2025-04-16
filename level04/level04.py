## Advent of code day 4

# Objective : 

import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.tools import parse_file

#--- Main functions --- #

def level04_part1(input_path) -> int: 

    # clean input file 
    input_list = parse_file(input_path).strip().splitlines()        # create a list of strings, each row is a string
    word_search = [list(row.strip()) for row in input_list]         # create a matrix of characters

    word = "XMAS"
    rows = len(word_search)
    cols = len(word_search[0])
    word_count = 0
    directions = [(1, 0),(-1, 0),(0, 1),(0, -1),(1, -1),(-1, 1),(-1, -1),(1, 1)]

    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if word_is_found(word_search, word, i, j, dx, dy):
                    word_count += 1

    return word_count


def level04_part2(input_path) -> int:
    word_count = 0
    return word_count



# #--- Utility functions --- #

def word_is_found(grid, word, i, j, dx, dy) ->bool:
    word_length = len(word)
    rows = len(grid)
    cols = len(grid[0])
    # for each grid character check if it matches a word character in all directions
    for k in range(word_length):
        x = i + k*dx
        y = j + k*dy
        if not (0 <= x < rows and 0 <= y < cols) or (grid[x][y]!=word[k]):  # prevent index of being out of bounds
            return False
    return True




#--- Main call --- #
def main():
    file_path = "level04_input.txt"
    result_part1 = level04_part1(file_path)
    #result_part2 = level04_part2(file_path)
    print("number of word found:", result_part1) 
    #print("":", result_part2)

if __name__ == "__main__":
    main()


