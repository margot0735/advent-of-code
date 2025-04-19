# Advent of Code 2024

This repository contains my solutions to the puzzles from the Advent of Code (https://adventofcode.com/) challenge, using pyton.    
Each level corresponds to a specific day of the challenge, with associated input files and scripts.  

## Installation  

To get started, clone the repository to your local machine:  

```bash
git clone https://github.com/margot0735/advent-of-code.git
cd advent-of-code  
```

## Project Structure

- `level01/`, `level02/`, `level03/`, `level04/`: Folders containing the Python solution script and the corresponding input file for each level.
- `tests/`: Folder containing functional tests for levels 2 to 4.
- `utils/tools.py`: Utility functions for input files.
- `run.py`: A script that runs all the level solutions and their associated tests.  

## Use

You can run all the solutions for each level as well as the associated tests with : `python run.py`  
You can run each level independently : `python levelXX/levelXX.py`
You can run each test independently : `pytest tests\test_levelXX.py 