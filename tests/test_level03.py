# file : test_level03.py
# description : functionnal test of level03 puzzles

import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from level03.level03 import level03_part1, level03_part2

def test_full_example(tmp_path):
    # Test example given in the advent of code"""

    input_data_part1 = """ 
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
    input_file_part1 = tmp_path / "input_part1.txt"
    input_file_part1.write_text(input_data_part1)
    assert level03_part1(str(input_file_part1)) == 161

    input_data_part2 = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""
    input_file_part2 = tmp_path / "input_part2.txt"
    input_file_part2.write_text(input_data_part2)
    assert level03_part2(str(input_file_part2)) == 48

# Launch tests with pytest
if __name__ == "__main__":
    pytest.main()