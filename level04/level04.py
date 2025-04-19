# file : level04.py
# description : Advent of code day 1## Advent of code day 4

import numpy as np
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.tools import parse_file

#--- Main functions --- #

def level04(input_path, part_id) -> int: 

    # clean input file 
    input_list = parse_file(input_path).strip().splitlines()        # create a list of strings, each row is a string
    word_search = [list(row.strip()) for row in input_list]         # create a matrix of characters


    rows, cols = len(word_search), len(word_search[0])
    word_count = 0

    match part_id:
        case 1:
            word = "XMAS"
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1), (-1, -1), (1, 1)]     #8 possible directions
            for i in range(rows):
                for j in range(cols):
                    for dx, dy in directions:
                        if word_is_found_part1(word_search, word, i, j, dx, dy):
                            word_count += 1

        case 2:
            word = "MAS"
            word_positions = [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]   
            directions = [(1, 1), (1, -1)]      #starting from (0,0), there is 2 possible directions = 2 diagonals
            for i in range(rows):
                for j in range(cols):
                    for dx, dy in directions:
                        if word_is_found_part2(word_search, word, word_positions, i, j, dx, dy):
                            word_count += 1
                            break  # only count 1 match

    return word_count


# #--- Utility functions --- #

def word_is_found_part1(grid, word, i, j, dx, dy) ->bool:
    word_length = len(word)
    rows = len(grid)
    cols = len(grid[0])
    # for each grid character check in all directions if it matches a word character 
    for k in range(word_length):
        x = i + k*dx
        y = j + k*dy
        if not (0 <= x < rows and 0 <= y < cols) or (grid[x][y]!=word[k]):  # prevent index of being out of bounds
            return False
    return True

def word_is_found_part2(grid, word, word_positions, i, j, dx, dy) -> bool:
    rows = len(grid)
    cols = len(grid[0])

    if grid[i][j] != word[1]:       # working for a 3 letters word
        return False

    # compute 2D pose of the extremity letters of the first diagonal
    x1, y1 = i - dx, j - dy
    x2, y2 = i + dx, j + dy
    if not (0 <= x1 < rows and 0 <= y1 < cols and 0 <= x2 < rows and 0 <= y2 < cols):   # check if index is not out of bounds
        return False
    diagonal1= grid[x1][y1], grid[x2][y2]

    # compute 2D pose of the extremity letters of the second diagonal
    x3, y3 = i - dy, j + dx
    x4, y4 = i + dy, j - dx
    if not (0 <= x3 < rows and 0 <= y3 < cols and 0 <= x4 < rows and 0 <= y4 < cols):   # check if index is not out of bounds
        return False
    diagonal2 = grid[x3][y3], grid[x4][y4]

    # Check if one diagonal is the word
    def diagonal_is_valid(diagonal) ->bool:
        return diagonal == (word[0], word[2]) or diagonal == (word[2], word[0])

    return diagonal_is_valid(diagonal1) and diagonal_is_valid(diagonal2)


#--- Main call --- #

def main():
    file_path = "level04_input.txt"
    result_part1 = level04(file_path,1)
    result_part2 = level04(file_path,2)
    print("number of 'XMAS' found:", result_part1) 
    print("number of X-shaped 'MAS' found:", result_part2)

if __name__ == "__main__":
    main()


