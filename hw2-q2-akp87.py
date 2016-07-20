# Homework 2: Simple Sudoku Solver with Local Search
# Author: Alyssa Plan
# Date: 07/20/2016

# importing numpy for array functionality.
import numpy

def printBoard(board):
    global horizontal_divider
    horizontal_divider= '-------------'
    print horizontal_divider
    for i, row in enumerate(board):
        print '|',
        for j, entry in enumerate(row):
            print entry,
            if(j == 1):
                    print '|',
        print '|',
        print
        if(i == 1):
            print horizontal_divider
    print horizontal_divider

# Main function. The lack of curly braces still throws me off.
def main():
    # Initialize board with entries
    simple_sudoku = numpy.array([[1, 0, 3, 0], [0, 0, 0, 0], [2, 0, 4, 0], [0, 0, 0, 0]])
    printBoard(simple_sudoku)


main()
