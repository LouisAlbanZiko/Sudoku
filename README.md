# Sudoku Solver

This is a project I did for uni.
Most of the code is written in python but I had to use ctypes for the windows implementation of moving the cursor because the command line doesn't support ANSI characters for moving the cursor.

### Setup
To run the project open a terminal/cmd, clone the repository and run main.py with python: `python main.py` (on linux it might be `python3 main.py` depending on what versions of python you have installed). Make sure you are using python3 and not python2. Python2 will not work!

### Features
- Prompt with different commands
- Load and save .sdk files
- Solves loaded sudokus
- Can change the interval between solving ticks for better visualisation or performance
