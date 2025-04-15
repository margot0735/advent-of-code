import numpy as np
import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from level03.level03_part1 import main

def test_full_example(tmp_path):
    # Exemple given in the advend of code
    input_data = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
    # Create a temporary file for the example
    input_file = tmp_path / "input.txt"
    input_file.write_text(input_data)
    # Verify the example statement
    assert main(str(input_file)) == 161

# Launch tests with pytest
if __name__ == "__main__":
    pytest.main()