from sudoku import Sudoku
import random


BOARD_SIZE = 9
SUBGRID_SIZE = 3

# Create population
def create_population(sudoku, population_size):
    population = []
    for individual in range(population_size):
        population.append(create_individual(sudoku))
    return population

def create_individual(sudoku):
    individual = Sudoku(sudoku)
    sudoku_solution = individual.solution
    
    # First, loop for decorator (init_state)
    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            random_val = random.randrange(1, 10)
            if (individual.sudoku[row][column] == 0):
                sudoku_solution[row][column] = random_val
            else:
                sudoku_solution[row][column] = sudoku[row][column]
    individual.solution = sudoku_solution
    return individual
# Calculate fitness
#def calculate_fitness():

# Order by fitness
# Selection
# Crossover
# Mutation
# 
sudo = [
        [8,6,0,2,4,7,5,0,0],
        [7,0,9,1,5,8,6,0,2],
        [2,5,0,9,6,3,1,0,8],
        [9,1,6,0,8,0,0,0,4],
        [0,8,0,0,3,6,9,0,0],
        [0,4,2,7,0,9,0,5,6],
        [0,2,8,0,9,5,4,1,7],
        [4,9,0,8,0,0,0,6,0],
        [0,0,0,6,0,4,3,8,0]]

pop = create_population(sudo, 5)

# Print population
#for i in pop:
#    i.print_solution()
#    i.print_sudoku()
#    print("\n")