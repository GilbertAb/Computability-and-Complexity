import copy
import random

BOARD_SIZE = 9
SUBGRID_SIZE = 3

class Sudoku:
    def __init__(self, rows):
        # Board with fixed values
        self.sudoku = []
        for row in range(len(rows)):
            self.sudoku.append(rows[row])
        
        # Board with solution
        self.solution = []
        for row in range(BOARD_SIZE):
            self.solution.append([])
            for column in range(BOARD_SIZE):
                self.solution[row].append(0)

    def print_board(self, board):
        print("\n|-------|-------|-------|")
        for row in range(BOARD_SIZE):
            for column in range(BOARD_SIZE):
                if (column % 3 == 2):
                    print(board[row][column], "| ", end="")
                elif (column == 0):
                    print("|", board[row][column], end=" ")
                else:
                    print(board[row][column], "", end="")
            if (row % 3 == 2):
                print("\n|-------|-------|-------|")
            else:
                print("")
    # Print board with fixed values
    def print_sudoku(self):
        self.print_board(self.sudoku)

    # Print board with solution
    def print_solution(self):
        self.print_board(self.solution)
    
    # Returns if solution's board is a valid solution
    def is_solution(self):
        # Check if there is any empty grid (0 value)
        is_solution = not self.empty_grid()

        # Check rows
        is_solution = not self.are_duplicated_in_rows(self.solution)
        
        # Check columns
        if is_solution != False:
            is_solution = not self.are_duplicated_in_columns()
        
        # Check 3x3 subgrids
        if is_solution != False:
            is_solution = not self.are_duplicated_in_subgrids()
        
        return is_solution

    # Returns True if there is an empty grid (equal 0) in the solution,
    # otherwise returns False
    def empty_grid(self):
        for row in self.solution:
            if 0 in row:
                return True
        return False
    # Returns True if there is any duplicated number in any row of the board,
    # otherwise returns false
    def are_duplicated_in_rows(self, board):
        duplicated = False
        for row in board:
            duplicated_nums = {num for num in row if row.count(num) > 1}
            # if there's any duplicated num in the row
            if (len(duplicated_nums) > 0 and not 0 in duplicated_nums):
                duplicated = True
                break
        return duplicated
    # Returns True if there is any duplicated number in any column of the board,
    # otherwise returns false
    def are_duplicated_in_columns(self):
        duplicated = False
        columns = [[],[],[],[],[],[],[],[],[]]
        # Extract and store columns
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):  
                columns[i].append(self.solution[j][i])
        # Check columns
        duplicated = self.are_duplicated_in_rows(columns)
        return duplicated
    
    # Returns True if there is any duplicated number in any 3x3 subgrid of the board,
    # otherwise returns false
    def are_duplicated_in_subgrids(self):
        duplicated = False
        subgrid = []
        # Scroll grid in rows
        for rgrid in range(SUBGRID_SIZE):
            # Scroll grid in columns
            for cgrid in range(SUBGRID_SIZE):
                if not duplicated:
                    # Make Subgrid
                    for row in range(SUBGRID_SIZE):
                        for column in range(SUBGRID_SIZE):
                            subgrid.append(self.solution[row + SUBGRID_SIZE*rgrid][column + SUBGRID_SIZE*cgrid])
                    # Check subgrid
                    duplicated = self.are_duplicated_in_3x3_subgrid(subgrid)
                    subgrid.clear()
                    if(duplicated):
                        break;
            
        return duplicated
    # Returns True if there is any duplicated number in an specific 3x3 subgrid of the board,
    # otherwise returns false
    def are_duplicated_in_3x3_subgrid(self, grid):
        duplicated = False
        duplicated_nums = {num for num in grid if grid.count(num) > 1 and num != 0}
        if (len(duplicated_nums) > 0 and not 0 in duplicated_nums):
            duplicated = True
        return duplicated 

    # Returns the amount of duplicated numbers in the solution
    # Is used to get the FITNESS for the genetic algorithm
    def count_duplicates(self):
        # Duplicates in rows
        duplicates = self.count_duplicates_in_rows(self.solution)   
        # Duplicates in columns
        columns = [[],[],[],[],[],[],[],[],[]]
        # Extract and store columns
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):  
                columns[i].append(self.solution[j][i])
        duplicates += self.count_duplicates_in_rows(columns)
        return duplicates
    
    # Returns the amount of duplicated numbers in the rows of the solution
    def count_duplicates_in_rows(self, board):
        duplicates = 0
        for row in board:
            duplicated_nums = {num for num in row if row.count(num) > 1}
            for dnum in duplicated_nums:
                duplicates += row.count(dnum)-1
        return duplicates
    
    # Returns the 3x3 subgrids of the solution
    def get_3x3_subgrids(self):
        subgrids = []
        subgrid = []
        # Scroll grid in rows
        for rgrid in range(SUBGRID_SIZE):
            # Scroll grid in columns
            for cgrid in range(SUBGRID_SIZE):
                # Make Subgrid
                for row in range(SUBGRID_SIZE):
                    for column in range(SUBGRID_SIZE):
                        subgrid.append(self.solution[row + SUBGRID_SIZE*rgrid][column + SUBGRID_SIZE*cgrid])
                # Check subgrid
                subgrids.append(copy.copy(subgrid))
                subgrid.clear()            
        return subgrids
    
    '''
    indexes of subgrids:
        |0|1|2|
        |3|4|5|
        |6|7|8|
    '''
    # Sets a new value (subgrid) to a 3x3 subgrid
    # Is used for CROSSOVER of the genetic algorithm
    def set_3x3_subgrid(self, subgrid, index):
        grid_row = 0
        if (index > 2 and index < 6):
            grid_row = 1
        elif (index >= 6 and index < 10):
            grid_row = 2
                
        subgrid_index = 0
        for row in range(SUBGRID_SIZE):
            for column in range(SUBGRID_SIZE):
                self.solution[row + SUBGRID_SIZE*grid_row][column + SUBGRID_SIZE*(index%3)] = subgrid[subgrid_index]
                subgrid_index += 1

    # Randomly swaps two values within a 3x3 subgrid
    # Is used for MUTATION of the genetic algorithm
    def swap_2_values(self, subgrid_index):
        if subgrid_index < 3:
            # 0 -> [0-2], [0-2] 
            # 1 -> [0-2], [3-5] 
            # 2 -> [0-2], [6-8] 
            self.swap(0)

        elif subgrid_index > 2 and subgrid_index < 6:
            # 3 -> [3-5], [0-2] 
            # 4 -> [3-5], [3-5] 
            # 5 -> [3-5], [6-8] 
            self.swap(1)
        elif subgrid_index > 5 and subgrid_index < 9:
            # 6 -> [6-8], [0-2] 
            # 7 -> [6-8], [3-5] 
            # 8 -> [6-8], [6-8] 
            self.swap(2)
    
    # Swap two values within a 3x3 subgrid
    # Grid_row is the row where the 3x3 subgrid is located (0, 1 or 2)
    def swap(self, grid_row):

        row_1 = random.randrange(0, 3) + grid_row*SUBGRID_SIZE
        column_1 = random.randrange(0, 3) + ((row_1 - grid_row*SUBGRID_SIZE) * SUBGRID_SIZE)
        row_2 = random.randrange(0, 3) + grid_row*SUBGRID_SIZE
        column_2 = random.randrange(0, 3) + ((row_1 - grid_row*SUBGRID_SIZE) * SUBGRID_SIZE)
        # Swap
        aux = self.solution[row_1][column_1]
        self.solution[row_1][column_1] = self.solution[row_2][column_2]
        self.solution[row_2][column_2] = aux
