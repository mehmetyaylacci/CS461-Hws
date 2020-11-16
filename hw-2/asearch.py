import numpy as np
import copy

class A_search:
    
    
    # constructor
    def __init__(self): 
        self.queue = []
        self.end_matrix = np.array([1,2,3,4, 2,3,4,5, 3,4,5,5, 4,5,5,0]).reshape(4,4)


    '''
    h1: number of misplaced tiles is used as heuristics
    calculating the number of misplaced tiles, by checking for the number of non-matching values
    adds 1 for every non-matching value of the initial matrix compared to the goal matrix
    '''
    def heuristics(self, state):
        answer = 0
        for x in range(4):
            for y in range(4):
                if state.matrix[y][x] == self.end_matrix[y][x]:
                    answer += 1
        return 16 - answer


    '''
    this function that starts the solver object to initiate the
    solving process of the given initial puzzle
    this method uses the continue_search method to continue on with
    the main part of the solving process
    '''
    def start_search(self, initial_puzzle):
        self.queue.append(initial_puzzle)
        visited = [] # stores every node that is visited through the search, in order to avoid repetition
        visited.append(self.id_func(initial_puzzle))
        self.continue_search(0, visited, 0)


    '''
    this function is the main function that we use to solve the
    given puzzle. it takes the depth argument which later equates
    to the number of steps to solve the puzzle, it takes the array
    of already visited puzzle states and also the total cost of the
    puzzle's solving procedure
    the method ends and prints the optimal path to solve the given 
    E15 puzzle
    '''
    def continue_search(self, depth, visited, total_cost):
        # the current puzzle object is kept for later reverts to the original state
        current_puzzle = self.queue[0]

        # we continue until we solve the puzzle
        while not (current_puzzle.matrix == self.end_matrix).all():
          current_puzzle = self.queue.pop(0)
          temp_puzzle = copy.deepcopy(current_puzzle)

          # movements in each direction represent the movement of the blank tile
          # here we use the heuristic function and the depth to calculate the cost
          # of each move that will be appended/added to the queue          
          if temp_puzzle.move_left():
            add_state = temp_puzzle 
            add_state.depth += 1
            add_state.cost = self.heuristics(add_state) + add_state.depth
            add_state.lastmove += ' 0 Left ->'
            self.queue.append(add_state)
          temp_puzzle = copy.deepcopy(current_puzzle)

          if temp_puzzle.move_right():
            add_state = temp_puzzle 
            add_state.depth += 1
            add_state.cost = self.heuristics(add_state) + add_state.depth
            add_state.lastmove += ' 0 Right ->'
            self.queue.append(add_state)
          temp_puzzle = copy.deepcopy(current_puzzle)
  
          if temp_puzzle.move_up():
            add_state = temp_puzzle
            add_state.depth += 1
            add_state.cost = self.heuristics(add_state) + add_state.depth
            add_state.lastmove += ' 0 Up ->'
            self.queue.append(add_state)
          temp_puzzle = copy.deepcopy(current_puzzle)
          
          if temp_puzzle.move_down():
            add_state = temp_puzzle
            add_state.depth += 1
            add_state.cost = self.heuristics(add_state) + add_state.depth
            add_state.lastmove += ' 0 Down ->'
            self.queue.append(add_state)
          temp_puzzle = copy.deepcopy(current_puzzle)

          # we remove repeated steps from the queue
          for an_item in self.queue:
            if self.id_func(an_item) in visited:
              self.queue.remove(an_item)

          self.queue = sorted(self.queue, key=lambda x: x.cost)
          visited.append(self.id_func(current_puzzle))

        else:
          print('\nFinal solved puzzle:\n')
          print(current_puzzle.matrix)
          print('I solved this puzzle in', current_puzzle.depth, 'steps')
          print(current_puzzle.lastmove + ' Solved!')
          return len(self.queue)


    '''
    this is the same function as the start_search function
    however it is only used to return the size of the queue
    so that we can graph it later in the main of the program
    '''
    def queue_sizes(self, initial_puzzle):
      self.queue.append(initial_puzzle)
      return self.qs_func(0, [], 0)


    '''
    qs_func resembles the continue_search function, however,
    it only returns the size of the queue
    '''
    def qs_func(self, depth, visited, total_cost):
      current_puzzle = self.queue[0]
      while not (current_puzzle.matrix == self.end_matrix).all():
        current_puzzle = self.queue.pop(0)
        temp_puzzle = copy.deepcopy(current_puzzle)
        if temp_puzzle.move_left():
          add_state = temp_puzzle 
          add_state.depth += 1
          add_state.cost = self.heuristics(add_state) + add_state.depth
          self.queue.append(add_state)
        temp_puzzle = copy.deepcopy(current_puzzle)
        if temp_puzzle.move_right():
          add_state = temp_puzzle 
          add_state.depth += 1
          add_state.cost = self.heuristics(add_state) + add_state.depth
          self.queue.append(add_state)
        temp_puzzle = copy.deepcopy(current_puzzle)
        if temp_puzzle.move_up():
          add_state = temp_puzzle
          add_state.depth += 1
          add_state.cost = self.heuristics(add_state) + add_state.depth
          self.queue.append(add_state)
        temp_puzzle = copy.deepcopy(current_puzzle)  
        if temp_puzzle.move_down():
          add_state = temp_puzzle
          add_state.depth += 1
          add_state.cost = self.heuristics(add_state) + add_state.depth
          self.queue.append(add_state)
        temp_puzzle = copy.deepcopy(current_puzzle)
        for an_item in self.queue:
          if self.id_func(an_item) in visited:
            self.queue.remove(an_item)
        self.queue = sorted(self.queue, key=lambda x: x.cost)
        visited.append(self.id_func(current_puzzle))
      else:
        return len(self.queue)


    '''
    this function gets a state object inside it and returns
    a string that will identify each unique states
    this function is used later in the main function (search function)
    to idetify which states are repeated
    '''
    def id_func(self, state):
      id_str = ""
      temp_array = np.array(state.matrix).flatten()
      for an_int in temp_array:
        id_str += str(an_int)
      return id_str


    '''
    reset function resets the puzzle object's assignments that were done in previous object
    method calls
    '''
    def reset(self):
      self.queue = []
