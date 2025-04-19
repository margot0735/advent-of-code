# file : tools.py
# description : utilities functions

import os
import sys

def verify_file(file_path):
    """function for verifying if txt file exists"""
    if not os.path.isfile(file_path):
        print(f"error : lists file '{file_path}' not found")
        sys.exit(1)

def parse_file(input_path) -> list:
    """function for reading txt file and returning the text in a list"""

    verify_file(input_path)

    with open(input_path, 'r') as file:
        input_list = file.read()

    return input_list