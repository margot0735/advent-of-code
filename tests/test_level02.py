import numpy as np
import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from level02.level02_part2 import verify_increasing, verify_decreasing, verify_level_difference, main

def test_verify_increasing():
    assert verify_increasing(np.array([1, 2, 3])) == True
    assert verify_increasing(np.array([1, 1, 2])) == False
    assert verify_increasing(np.array([3, 2, 1])) == False

def test_verify_decreasing():
    assert verify_decreasing(np.array([5, 3, 1])) == True
    assert verify_decreasing(np.array([5, 5, 4])) == False
    assert verify_decreasing(np.array([1, 2, 3])) == False

def test_verify_level_difference():
    assert verify_level_difference(np.array([1, 2, 3])) == True
    assert verify_level_difference(np.array([1, 4])) == True  # 4 - 1 = 3 ok
    assert verify_level_difference(np.array([1, 5])) == False  # 4 = too much
    assert verify_level_difference(np.array([1, 2, 6])) == False

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
    assert main(str(input_file)) == 4

# Launch tests with pytest
if __name__ == "__main__":
    pytest.main()
