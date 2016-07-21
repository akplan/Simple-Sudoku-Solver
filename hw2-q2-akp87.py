# Homework 2: Simple Sudoku Solver with Local Search
# Author: Alyssa Plan
# Date: 07/20/2016

from random import random, randint
from copy import deepcopy

class SudokuBoard:
    def __init__(self,board):
        self.board = deepcopy(board)
        self.fitness = 0
        self.generateAnswer()

    # returns a list of lists of rows in the board.
    # (mostly here to look pretty)
    def getRows(self):
        rows = self.board
        return rows

    # returns a list of lists of columns in the board.
    def getColumns(self):
        columns = [list(a) for a in zip(*self.board)]
        return columns

    # returns a list of lists of all box entries in the board.
    def getBoxes(self):
        coords = [(x % 2, x / 2) for x in range(0,4)]
        boxes = [[self.board[x*2+xx][y*2+yy] for xx, yy in coords] for x,y in coords]
        return boxes

    # Generates a random sudoku solution that may/may not be correct.
    def generateAnswer(self):
        for row in self.board:
            for k, entry in enumerate(row):
                if(entry == 0):
                    row[k] = randint(1,4)
        self.fitness = self.generateFitness()

    # Prints the board.
    def printBoard(self):
        global horizontal_divider
        horizontal_divider= '-------------'
        print horizontal_divider
        for i, row in enumerate(self.board):
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
    # defines whether a row, column, or box of the row is valid
    def isValid(self, block):
        return 4 == len(set(block))

    # Generates how fit the solution is.
    def generateFitness(self):
        fitness = 0
        rows = self.getRows()
        for row in rows:
            if self.isValid(row):
                fitness += 1
        columns = self.getColumns()
        for column in columns:
            if self.isValid(column):
                fitness += 1
        boxes = self.getBoxes()
        for box in boxes:
            if self.isValid(box):
                fitness += 1
        fitness = 12-fitness
        return fitness

# ================================
# FUNCTIONS FOR GENETIC ALGORITHMS
# ================================

# generates a population to be used.
def generatePopulation(board,count):
    population = []
    for x in xrange(count):
        x = SudokuBoard(board)
        population.append(x)
    return population

# returns the average fitness of a population.
def averageFitness(pop):
    summed = 0
    for board in pop:
        summed += board.fitness
    return summed / (len(pop) * 1.0)

# ranks your population by fitness
def rankPopulation(pop):
    ranked = [(k.fitness, k) for k in pop] # create tuple weighed by fitness
    ranked = [k[1] for k in sorted(ranked)]
    return ranked

# moves board to the next generation, hopefully a better one.
def evolve(pop,init_board):
    currentFitness = averageFitness(pop)
    mutate_prob = 0.07 # probability to mutate
    retain = 0.2 # probability of how much we're keeping
    randselect = 0.05 # chance to randomly select

    ranked = rankPopulation(pop)
    retained_length = int(len(ranked)*retain)
    parents = ranked[:retained_length]
    # print parents
    # add random to new population
    for board in ranked[:retained_length]:
        if randselect > random():
            parents.append(board)

    # mutate boards
    for board in parents:
        if mutate_prob > random():
            rand_row = randint(0,len(board.board)-1)
            rand_col = randint(0,len(board.board[0])-1)

            while(init_board[rand_row][rand_col] != 0):
                rand_row = randint(0,len(board.board)-1)
                rand_col = randint(0,len(board.board[0])-1)
            board.board[rand_row][rand_col] = randint(1,4)
            board.generateFitness()

    # crossover
    num_parents = len(parents)
    free_space = len(pop) - num_parents
    children = []
    while len(children) < free_space:
        parents1 = randint(0, num_parents-1)
        parents2 = randint(0, num_parents-1)

        if parents1 != parents2:
            parent1 = parents[parents1]
            parent2 = parents[parents2]
            half = 2
            if 0.49 > random():
                child = SudokuBoard(parent1.board[:half] + parent2.board[half:])
            else:
                childboard = []
                for row in parent1.board:
                    currentRow = row[:half]
                    currentRow.extend(row[half:])
                    childboard.append(currentRow)
                child = SudokuBoard(childboard)
            children.append(child)
    parents.extend(children)

    # mutate boards
    for board in parents:
        if mutate_prob > random():
            rand_row = randint(0,len(board.board)-1)
            rand_col = randint(0,len(board.board[0])-1)

            while(init_board[rand_row][rand_col] != 0):
                rand_row = randint(0,len(board.board)-1)
                rand_col = randint(0,len(board.board[0])-1)
            board.board[rand_row][rand_col] = randint(1,4)
            board.generateFitness()
    return parents



# Main function. The lack of curly braces still throws me off.
def main():
    # Initialize board with entries
    init_board = [[1, 0, 3, 0], [0, 0, 0, 0], [2, 0, 4, 0], [0, 0, 0, 0]]
    pop = generatePopulation(init_board,150)
    maxFitness = rankPopulation(pop)[0].fitness
    print maxFitness
    rankPopulation(pop)[0].printBoard()
    for i in xrange(750):
        pop = evolve(pop,init_board)
        rankedpop = rankPopulation(pop)
        if rankedpop[0].fitness < maxFitness:
            rankedpop[0].printBoard()
            print 'new number of penalties:',
            print rankedpop[0].fitness
            maxFitness = rankedpop[0].fitness


main()
