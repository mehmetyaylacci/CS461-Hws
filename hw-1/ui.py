# @authors: 
# Burak Turksever
# Mehmet Yaylaci
# Eralp Kumbasar
from state import State
import networkx as nx
import matplotlib.pyplot as plt

class Graph:

  # the function that initiates the search with the given number of
  # cannibals and missionaries as well as the capacity of the boat 
  def DFS_start(self, number, boat_capacity):
    '''
    the function initializes the DFS with the given number of cannibals and missionaries as well as the capacity of the boat 
    '''
    self.G = nx.Graph()
    final_string = [] #will be used as the output string when goal state is reached
    existingStates = [] #keeps the visited states
    start = State(number, number, 0, 0, "left", boat_capacity) #creates the starting state with given number of cann and miss at left, 0 of them at right, boat starting at left with the given capacity
    goal_state_id = self.id_func(State(0, 0, number, number, "right", boat_capacity)) #defines goal state as transferring all people to the right
    self.DFS(start, 0, existingStates, goal_state_id, final_string) #calls DFS with starting state
    for i in range(len(final_string)-1, -1, -1):
      print(final_string[i])

  # 
  def DFS(self, currState, depth, existingStates, goal_state_id, final_string):
    '''
    recursive depth first search to traverse to the goal state
    adds current state to existingStates for checking
    uses the id_func function to understand if the currState (current state) object already has been visited and removes the newly generated next state objects that are redundant/repeated
    afterwards, the function initiates itself (recurses)by using the chosen next state until a goal state is found
    only the nodes that lead to the answer are printed
    limitations: Python has a recursion depth limit hence we can not have more than 494 missionaries and cannibals at once
    '''
    depth += 1
    next_states = self.next_state_gen(currState) #creates next states for the current state
    if self.id_func(currState) == goal_state_id:
      next_states = []
      return True #when goal is reached clears next states and returns True 
    elif depth == 1 and currState.left_c + currState.left_m <= currState.boat:
      print("The boat capacity is enough to carry all the passengers at once.")
      return True #if one transfer is enough immediately finish and return True
    else:
      existingStates.append(self.id_func(currState))
      for check_state in next_states:
        if self.id_func(check_state) in existingStates:
          next_states.remove(check_state) #removes any visited states from next states to prevent repetitions and loops
      for temp_state in next_states:
        # print(str(temp_state))
        if self.id_func(temp_state) not in existingStates:#if one of the next states not previously visited give the goal state after the recursive call, return True
          if self.DFS(temp_state, depth, existingStates, goal_state_id, final_string):
            self.G.add_node(temp_state)
            self.G.add_edge(temp_state, currState, lenght = 100)
            constructed_str = "\nDepth:" + str(depth) + "\nCurrent Node: " + str(temp_state) 
            final_string.append(constructed_str)
            return True
    return False
  

  def next_state_gen(self, passed_state):
    '''
    next state generator that generates every possible path BUT
    only considers the ones that point towards the solution and those that are valid
    possible improvements: reversing the generation so that the amount of missionaries and cannibals in the first outputted generation is maximized
    '''
    states_array = []
    #if boat is at left for example, it takes away miss/cann from left to the right, so num of miss/cann decreases at left, and increases at right
    #same is done the other way when boat is at right
    #multiplier is used for that purpose, and it has opposite signs in the eq for left and right
    if passed_state.boat_pos == "left":
      multiplier = -1
      new_boat_pos = "right"
    else:
      multiplier = 1
      new_boat_pos = "left"
    for cannibal in range(0, passed_state.boat + 1):
      for missionary in range(0, passed_state.boat + 1):
        if (missionary + cannibal <=  passed_state.boat and missionary + cannibal > 0 and cannibal <= missionary) or (missionary + cannibal <=  passed_state.boat and missionary + cannibal > 0 and cannibal > 0 and missionary == 0):#iterating through all possible values for number missionaries and cannibals, so generates all possible further states
          left_c = multiplier * cannibal
          left_m = multiplier * missionary
          right_c = -(multiplier) * cannibal
          right_m = -(multiplier) * missionary
          add_state = State(passed_state.left_c + left_c, passed_state.left_m + left_m, passed_state.right_c + right_c, passed_state.right_m + right_m, new_boat_pos, passed_state.boat)
          #adding a new next state according to lastly updated values of miss/cann
          if add_state.check_possible():
            states_array.append(add_state)
    return states_array


  def id_func(self, passed_state):
    '''
    identification function to identify known nodes 
    works by concatenating the state missionary, cannibal and boat position values one after the other
    it allows the program to check for repeated steps by comparison to existing states in DFS
    with this algorithm, a step is NEVER repeated
    '''
    constructed_str = str(passed_state.left_c) + str(passed_state.left_m) + str(passed_state.right_c) + str(passed_state.right_m) + str(passed_state.boat_pos)
    return constructed_str

  def draw_graph(self):
    nx.draw(self.G, with_labels = True, node_size = 50)
    plt.draw()
    plt.show()