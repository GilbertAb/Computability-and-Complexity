# Se tomó de referencia el pseudocódigo de https://es.wikipedia.org/wiki/Ramificación_y_poda

class Node:
  def __init__(self):
    self.row = 0
    self.column = 0
    self.solution = []

class Sudoku_BB:
  def __init__(self, sudoku):
    self.poss_solutions_queue = [] # Node queue
    self.node = Node() 

    self.node.solution = sudoku
    self.poss_solutions_queue.append(self.node)

    while(len(self.poss_solutions_queue) > 0):
      temp = self.poss_solutions_queue.pop()
      if temp.solution[temp.row][temp.column] == 0:
        for index in range(1, 9, 9):
          temp.solution[temp.row][temp.column] = index
          if (not self.is_number_in_row(temp.row, index) and
              not self.is_number_in_column(temp.column, index) and
              not self.is_number_in_3x3_subgrid(temp.row, temp.column, index)):
            # casos
            self.node2 = Node()
            if temp.row < 9 and temp.column == 9:
              self.node2.solution = temp.solution
              self.node2.row = temp.row + 1
              self.node2.column = 1
              self.poss_solutions_queue.append(self.node2)            
            elif temp.row <= 9 and temp.column < 9:
              self.node2.solution = temp.solution
              self.node2.row = temp.row
              self.node2.column = temp.column + 1
              self.poss_solutions_queue.append(self.node2)

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

sudo = [
      [0,6,0,  2,4,7,  5,0,0],
      [7,0,9,  1,5,8,  6,0,2],
      [2,5,0,  9,6,3,  1,0,8],

      [9,1,6,  0,8,0,  0,0,4],
      [0,8,0,  0,3,6,  9,0,0],
      [0,4,2,  7,0,9,  0,5,6],

      [0,2,8,  0,9,5,  4,1,7],
      [4,9,0,  8,0,0,  0,6,0],
      [0,0,0,  6,0,4,  3,8,0]]

s = Sudoku_BB(sudo)
