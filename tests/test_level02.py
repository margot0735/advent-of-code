# file : test_level02.py
# description : functionnal test of level02 puzzles

import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from level02.level02 import is_increasing, is_decreasing, has_valid_level_difference, level02

def test_full_example(tmp_path):
    # Exemple given in the advend of code
    input_data = """
    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    """
    # Create a temporary file for the example
    input_file = tmp_path / "input.txt"
    input_file.write_text(input_data)
    # Verify the example statement
    assert level02(str(input_file),False) == 2
    assert level02(str(input_file),True) == 4


# Launch tests with pytest
if __name__ == "__main__":
    pytest.main()
