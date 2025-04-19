import numpy as np
import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from level04.level04 import level04_part1, level04_part2

def test_full_example(tmp_path):
    # Test example given in the advent of code"""

    input_data = """
        MMMSXXMASM
        MSAMXMSMSA
        AMXSXMAAMM
        MSAMASMSMX
        XMASAMXAMM
        XXAMMXXAMA
        SMSMSASXSS
        SAXAMASAAA
        MAMMMXMMMM
        MXMXAXMASX
    """
    input_file = tmp_path / "input.txt"
    input_file.write_text(input_data)
    assert level04_part1(str(input_file)) == 18

    assert level04_part2(str(input_file)) == 9

# Launch tests with pytest
if __name__ == "__main__":
    pytest.main()