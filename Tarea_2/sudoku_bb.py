class Node:
  def __init__(self):
    self.row = 0
    self.column = 0
    self.solution = []

class Sudoku_BB:
  def __init__(self, sudoku):
    self.poss_solutions_queue = [] # Node queue
    self.first = Node() # X
    self.second = Node() # Y
    self.matrix = [] # Boolean matrix

    self.first.solution = sudoku
    self.poss_solutions_queue.append(self.first)

    for index in range(9):
      for subindex in range(9):
        if (sudoku[index][subindex] != 0):
          self.matrix[index][subindex] = False
        else:
          self.matrix[index][subindex] = True


    while(len(self.poss_solutions_queue) > 0):
      temp = self.poss_solutions_queue.pop(0)
      if not self.matrix[temp.row][temp.column]:
        for index in range(9):
          temp.solution[temp.row][temp.column] = index
          if (self.is_good_option(temp.row, temp.column)):
            # casos
            print("TEST")
      elif self.matrix[temp.row][temp.column]:
        # Casos
        print("TEST2")

  def is_good_option(self, row, column):
    # Evaluar por fila, por columna y por subgrupo
      # Es la misma idea que en el sudoku de fuerza bruta
    return True


      











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