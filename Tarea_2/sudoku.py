import copy

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
    
    def print_sudoku(self):
        self.print_board(self.sudoku)
    
    def print_solution(self):
        self.print_board(self.solution)
    

    def is_solution(self):
        # Check if there is any empty grid (0 value)
        is_solution = not self.empty_grid()

        # Check rows
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
                #print(duplicated_nums)
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
        #print(duplicates)
        return duplicates
        
    def count_duplicates_in_rows(self, board):
        duplicates = 0
        for row in board:
            duplicated_nums = {num for num in row if row.count(num) > 1}
            for dnum in duplicated_nums:
                duplicates += row.count(dnum)-1
        return duplicates

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
                #print(subgrid)
                subgrids.append(copy.copy(subgrid))
                subgrid.clear()            
        return subgrids
    '''
    indexes of subgrids:
        |0|1|2|
        |3|4|5|
        |6|7|8|
    '''
    def set_3x3_subgrid(self, subgrid, index):
        grid_row = 0
        if (index > 2 and index < 6):
            grid_row = 1
        elif (index >= 6 and index < 10):
            grid_row = 2
        grid_col = 0
        subgrid_index = 0
        for row in range(SUBGRID_SIZE):
            for column in range(SUBGRID_SIZE):
                #print("SUBi",subgrid_index)
                self.solution[row + SUBGRID_SIZE*grid_row][column + SUBGRID_SIZE*(index%3)] = subgrid[subgrid_index]
                subgrid_index += 1
        #self.print_solution()

# Test count duplicates
#sudo = [
#        [2,8,9,3,6,4,6,9,3],
#        [5,3,7,5,9,2,8,2,4],
#        [6,4,1,8,1,7,7,1,5],
#        [3,7,1,6,8,1,6,5,1],
#        [2,8,6,9,3,7,7,4,8],
#        [9,5,4,5,4,2,9,3,2],
#        [8,7,5,1,2,4,4,3,9],
#        [2,6,1,9,5,3,6,8,7],
#        [9,4,3,8,7,6,5,2,1]]

#sudo = [
#        [8,6,0,2,4,7,5,0,0],
#        [7,0,9,1,5,8,6,0,2],
#        [2,5,0,9,6,3,1,0,8],
#        [9,1,6,0,8,0,0,0,4],
#        [0,8,0,0,3,6,9,0,0],
#        [0,4,2,7,0,9,0,5,6],
#        [0,2,8,0,9,5,4,1,7],
#        [4,9,0,8,0,0,0,6,0],
#        [0,0,0,6,0,4,3,8,0]]

sudo = [
        [8,6,1,2,4,7,5,9,3],
        [7,3,9,1,5,8,6,4,2],
        [2,5,4,9,6,3,1,7,8],
        [9,1,6,5,8,2,7,3,4],
        [5,8,7,4,3,6,9,2,1],
        [3,4,2,7,1,9,8,5,6],
        [6,2,8,3,9,5,4,1,7],
        [4,9,3,8,7,1,2,6,5],
        [1,7,5,6,2,4,3,8,9]]

#s = Sudoku(sudo)
#s.solution = sudo
#s.get_3x3_subgrids()
#s.set_3x3_subgrid([1,2,3,4,5,6,7,8,9],0)


#s.count_duplicates()
#s.print_sudoku()
#print(s.is_solution())
#print(s.are_duplicated_in_rows(s.solution))
#print(s.are_duplicated_in_columns())
#print(s.are_duplicated_in_subgrids())