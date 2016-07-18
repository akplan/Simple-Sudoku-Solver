# Homework 2: Simple Sudoku Solver with Local Search
# Author: Alyssa Plan


# Function for printing the board as a grid.
# Lists are very foreign to me still.
def print_board(board):
    for row in board:
        for entry in row:
            print entry,
        print

# Main function. The lack of parenthesis still throws me off.
def main():
    # Initialize board with entries
    simple_sudoku = [[1, 0, 3, 0], [0, 0, 0, 0], [2, 0, 4, 0], [0, 0, 0, 0]]

    # Printing board for debug purposes, my python skills are
    # hardly skills yet
    # print "yarr how do i python"
    print_board(simple_sudoku)


main()
