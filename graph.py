from state import State
from time import sleep

class Graph:
  
  def __init__(self):
    G = nx.Graph()
    
  # Function for adding a node to the graph
  def add_to_graph(self, starting_vertex, neighbor_vertex):
    G.add_node(neighbor_vertex)
    G.add_edge(starting_vertex, neighbor_vertex)
  
  def DFS_start(self, number, boat_capacity):
    existingStates = []
    start = State(number, number, 0, 0, "left", boat_capacity)
    self.DFS(start, 0, existingStates)

  # recursive depth first search to traverse to the goal state
  def DFS(self, currState, depth, existingStates):
    depth+=1
    existingStates.append(currState)
    # sleep(1)
    if currState.isGoalState():
      return True
    else:
      next_states = self.buraks_next_state_gen(currState)
      # print(next_states)
      for temp_state in next_states:
        # print(temp_state)
        # print(existingStates)
        for check_state in existingStates:
          print(check_state)
          if not check_state.left_c == temp_state.left_c and not check_state.left_m == temp_state.left_m and not check_state.right_c == temp_state.right_c and not check_state.right_m == temp_state.right_m and not check_state.boat == temp_state.boat:
            print('Current node: ', str(temp_state), '\nDepth :', depth)
            self.DFS(temp_state, depth, existingStates)
    return False  
  
  def next_state_generator(self, aState):
    states_array = []
    for cannibal in range(aState.boat):
      for missionary in range(aState.boat):
        # we will make sure boat is possible here
        if missionary + cannibal <= aState.boat and missionary >= cannibal and missionary + cannibal > 0:
            
          aState.temp_l_c = aState.left_c
          aState.temp_l_m = aState.left_m
          aState.temp_r_c = aState.right_c
          aState.temp_r_m = aState.right_m
          aState.temp_pos = aState.boat_pos

          if aState.boat_pos == "right":
            aState.temp_r_m -= missionary
            aState.temp_r_c -= cannibal
            aState.temp_l_m += missionary
            aState.temp_l_c += cannibal
            aState.temp_pos = "left"
            
          elif aState.boat_pos == "left":
            aState.temp_r_m += missionary
            aState.temp_r_c += cannibal
            aState.temp_l_m -= missionary
            aState.temp_l_c -= cannibal
            aState.temp_pos = "right"
          
          add_state = State(aState.temp_l_c, aState.temp_l_m,aState.temp_r_c,aState.temp_r_m, aState.temp_pos, aState.boat)

          if add_state.check_possible():
            states_array.append(add_state)
            
    return states_array

  def buraks_next_state_gen(self, passed_state):
    states_array = []
    if passed_state.boat_pos == "left":
      multiplier = -1
      new_boat_pos = "right"
    else:
      multiplier = 1
      new_boat_pos = "left"
    for cannibal in range(0, passed_state.boat + 1):
      for missionary in range(0, passed_state.boat + 1):
        if missionary + cannibal <=  passed_state.boat and missionary + cannibal > 0:
            left_c = multiplier * cannibal
            left_m = multiplier * missionary
            right_c = -(multiplier) * cannibal
            right_m = -(multiplier) * missionary
            # print("leftc", left_c, "leftm", left_m)
            # print("rightc", right_c, "right", right_m)
            add_state = State(passed_state.left_c + left_c, passed_state.left_m + left_m, passed_state.right_c + right_c, passed_state.right_m + right_m, new_boat_pos, passed_state.boat)
            # print(str(add_state))
            if add_state.check_possible():
              # print(str(add_state))
              states_array.append(add_state)
    return states_array
            



"""
    empty() – Returns whether the stack is empty – Time Complexity : O(1)
    size() – Returns the size of the stack – Time Complexity : O(1)
    top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
    push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
    pop() – Deletes the top most element of the stack – Time Complexity : O(1)
"""