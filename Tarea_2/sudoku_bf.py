import time

BOARD_SIZE = 9
SUBGRID_SIZE = 3

class Sudoku_BF:
    def __init__(self, rows):
        self.solution = []
        for row in range(len(rows)):
            self.solution.append(rows[row])
  
    def print_sudoku(self):
        for row in self.solution:
            print(row)
    
    def is_solution(self):
        # Check if there is any empty grid (0 value)
        is_solution = not self.empty_grid()
        
        # Check rows
        if is_solution != False:
            is_solution = not self.are_duplicated_in_rows(self.solution)
        #print("ROWS: ", is_solution)
        
        # Check columns
        if is_solution != False:
            is_solution = not self.are_duplicated_in_columns()
        #print("COLUMNS: ", is_solution)
        
        # Check 3x3 subgrids
        if is_solution != False:
            is_solution = not self.are_duplicated_in_subgrids()
        #print("GRIDS: ", is_solution)
        
        return is_solution

    def empty_grid(self):
        for row in self.solution:
            if 0 in row:
                return True
        return False

    def are_duplicated_in_rows(self, board):
        duplicated = False
        for row in board:
            duplicated_nums = {num for num in row if row.count(num) > 1}
            # if there's any duplicated num in the row
            if (len(duplicated_nums) > 0 and not 0 in duplicated_nums):
                duplicated = True
                print(duplicated_nums)
                break
        return duplicated
    
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

    def are_duplicated_in_3x3_subgrid(self, grid):
        duplicated = False
        duplicated_nums = {num for num in grid if grid.count(num) > 1}
        if (len(duplicated_nums) > 0 and not 0 in duplicated_nums):
            duplicated = True
        return duplicated 

    def is_number_in_row(self, row, number):
        for i in range(9):
            if (number == self.solution[row][i]):
                return True
        return False
    
    def is_number_in_column(self, column, number):
        for i in range(9):
            if (number == self.solution[i][column]):
                return True
        return False
    
    def is_number_in_subgrids(self, row, column, number):
        isNumber = False
        first_index_block = row // 3
        second_index_block = column // 3

        beginning = first_index_block * 3
        final = second_index_block * 3

        subgrid = []
        for index in range(beginning, beginning + 3):
            for subindex in range(final, final + 3):
                subgrid.append(self.solution[index][subindex])

        isNumber = self.is_number_in_3x3_subgrid(subgrid, number)

        return isNumber

    def is_number_in_3x3_subgrid(self, grid, number): 
        is_number = False       
        for index in range(len(grid)):
            if grid[index] == number:
                is_number = True       
        return is_number

    def resolve(self):        
        return self.resolve_recursive(0,0)

    def resolve_recursive(self, row, column):        
        if row == 8 and column == 9:
            return True

        if column == 9:
            return self.resolve_recursive(row + 1, 0)

        if self.solution[row][column] == 0:
            for index in range(1, 10, 1):
                if (not self.is_number_in_row(row, index) and
                not self.is_number_in_column(column, index) and
                not self.is_number_in_subgrids(row, column,index)):
                    self.solution[row][column] = index

                    if self.resolve_recursive(row, column + 1):
                        return True
                self.solution[row][column] = 0                             
        else:
            return self.resolve_recursive(row, column + 1)   
        
        return False
                
sudo = [
       [8,6,0,  2,4,7,  5,0,0],
       [7,0,9,  1,5,8,  6,0,2],
       [2,5,0,  9,6,3,  1,0,8],

       [9,1,6,  0,8,0,  0,0,4],
       [0,8,0,  0,3,6,  9,0,0],
       [0,4,2,  7,0,9,  0,5,6],

       [0,2,8,  0,9,5,  4,1,7],
       [4,9,0,  8,0,0,  0,6,0],
       [0,0,0,  6,0,4,  3,8,0]]

# sudo = [
#         [8,6,1,2,4,7,5,9,3],
#         [7,3,9,1,5,8,6,4,2],
#         [2,5,4,9,6,3,1,7,8],
#         [9,1,6,5,8,2,7,3,4],
#         [5,8,7,4,3,6,9,2,1],
#         [3,4,2,7,1,9,8,5,6],
#         [6,2,8,3,9,5,4,1,7],
#         [4,9,3,8,7,1,2,6,5],
#         [1,7,5,6,2,4,3,8,9]]

s = Sudoku_BF(sudo)
start = time.time()
s.resolve()
end = time.time()
print("TIME: ", end-start, "seconds")
if s.is_solution():
    s.print_sudoku()
    print("ITS A SOLUTION")
else:
    s.print_sudoku()
    print("Is not a solution")