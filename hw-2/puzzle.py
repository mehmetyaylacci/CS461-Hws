import numpy as np
class Puzzle:

  # constructor when a matrix is supplied
  def __init__(self, matrix):
    self.matrix = matrix.reshape(4, 4)
    self.depth = 0
    self.cost = 0
    self.lastmove = ""


  # constructor when a matrix is not supplied
  def __init__(self):
    self.matrix = np.array([1,2,3,4, 2,3,4,5, 3,4,5,5, 4,5,5,0]).reshape(4,4)
    self.depth = 0
    self.cost = 0
    self.lastmove = ""
  

  '''
  function to move the zero tile to the left
  it only works if it can move left, hence if
  it is inside the boundaries after the movement
  the function returns true if it can move and has moved
  and false if it can't move
  '''
  def move_left(self):
    i = self.get_index_zero()
    if i[1] > 0:
      self.matrix[i[0]][i[1]], self.matrix[i[0]][i[1]-1] = self.matrix[i[0]][i[1]-1], self.matrix[i[0]][i[1]]
      return True
    return False


  '''
function to move the zero tile to the right
  it only works if it can move right, hence if
  it is inside the boundaries after the movement
  the function returns true if it can move and has moved
  and false if it can't move  
  '''
  def move_right(self):
    i = self.get_index_zero()
    if i[1] < 3:
      self.matrix[i[0]][i[1]], self.matrix[i[0]][i[1]+1] = self.matrix[i[0]][i[1]+1], self.matrix[i[0]][i[1]]
      return True
    return False


  '''
  function to move the zero tile to up
  it only works if it can move up, hence if
  it is inside the boundaries after the movement
  the function returns true if it can move and has moved
  and false if it can't move
  '''
  def move_up(self):
    i = self.get_index_zero()
    if i[0] > 0:
      self.matrix[i[0]][i[1]], self.matrix[i[0]-1][i[1]] = self.matrix[i[0]-1][i[1]], self.matrix[i[0]][i[1]]
      return True
    return False


  '''
  function to move the zero tile to down
  it only works if it can move down, hence if
  it is inside the boundaries after the movement
  the function returns true if it can move and has moved
  and false if it can't move
  '''
  def move_down(self):
    i = self.get_index_zero()
    if i[0] < 3:
      self.matrix[i[0]][i[1]], self.matrix[i[0]+1][i[1]] = self.matrix[i[0]+1][i[1]], self.matrix[i[0]][i[1]]
      return True
    return False


  '''
  function to return the index value of the blank tile(zero tile) on the matrix, as a tuple
  the first element of the tuple corresponds to the (row number - 1), or in other words,
  numbering the rows from 0 to 3, and the second element corresponds to the (column number - 1),
  from 0 to 3
  '''
  def get_index_zero(self):
    i = [np.where(self.matrix == 0)[0][0], np.where(self.matrix == 0)[1][0]]
    return i


  '''
  function to scramble the puzzle by doing 10 random movements
  however, this function won't increment the number of times that 
  there has been a random movement (i) if it couldn't move, in other words,
  if move functions are False, it doesn't increment (i)
  '''
  def scramble(self):
    i = 0
    while i < 10:
      rand = np.random.randint(4) + 1
      if rand == 1 and self.move_up():
        i+=1
      elif rand == 2 and self.move_right():
        i+=1
      elif rand == 3 and self.move_down():
        i+=1
      elif rand == 4 and self.move_left():
        i+=1