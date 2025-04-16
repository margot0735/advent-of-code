import numpy as np
import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from level04.level04 import level04_part1, level04_part2

def test_full_example(tmp_path):
    # Test example given in the advent of code"""

    input_data_part1 = """
    ....XXMAS.
    .SAMXMS...
    ...S..A...
    ..A.A.MS.X
    XMASAMX.MM
    X.....XA.A
    S.S.S.S.SS
    .A.A.A.A.A
    ..M.M.M.MM
    .X.X.XMASX
    """
    input_file_part1 = tmp_path / "input_part1.txt"
    input_file_part1.write_text(input_data_part1)
    assert level04_part1(str(input_file_part1)) == 18

    # input_data_part2 = 
    # input_file_part2 = tmp_path / "input_part2.txt"
    # input_file_part2.write_text(input_data_part2)
    # assert level04_part2(str(input_file_part2)) == 48

# Launch tests with pytest
if __name__ == "__main__":
    pytest.main()