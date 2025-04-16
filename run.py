# run.py

import level01.level01_part1
import level01.level01_part2

from level02.level02 import level02_part1, level02_part2

from level03.level03 import level03_part1, level03_part2

import tests.test_level02
import tests.test_level03

import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def run_all():
     
    file_path_level01 = os.path.join("level01", "level01_input.txt")
    file_path_level02 = os.path.join("level02", "level02_input.txt")
    file_path_level03 = os.path.join("level03", "level03_input.txt")

    print("result of level01 part 1 :" , level01.level01_part1.main(file_path_level01))
    print("result of level01 part 2 :" ,level01.level01_part2.main(file_path_level01))
    
    print("result of level02 part 1 :" ,level02_part1(file_path_level02))
    print("result of level02 part 2 :" ,level02_part2(file_path_level02))

    print("result of level03 part 1 :" ,level03_part1(file_path_level03))
    print("result of level03 part 2 :" ,level03_part2(file_path_level03))


    pytest.main()

if __name__ == '__main__':
    run_all()
