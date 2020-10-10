from state import State
from time import sleep

class Graph:
  
  # G = nx.Graph()
  # def __init__(self):
    
  # Function for adding a node to the graph
  # def add_to_graph(self, starting_vertex, neighbor_vertex):
  #    G.add_node(neighbor_vertex)
  #    G.add_edge(starting_vertex, neighbor_vertex)
  
  def DFS_start(self, number, boat_capacity):
    existingStates = []
    start = State(number, number, 0, 0, "left", boat_capacity)
    existingStates.append(start)
    self.DFS(start, 0, existingStates)


  # recursive depth first search to traverse to the goal state
  def DFS(self, currState, depth, existingStates):
    
    depth+=1
    # sleep(1)
    if currState.isGoalState():
      return True
    else:
      next_states = self.next_state_generator(currState)
      for temp_state in next_states:
        existingStates.append(temp_state)
        # print(existingStates)
      for check_state in existingStates:
        if not check_state.left_c == temp_state.left_c and not check_state.left_m == temp_state.left_m and not check_state.right_c == temp_state.right_c and not check_state.right_m == temp_state.right_m and not check_state.boat == temp_state.boat:
          # print('Current node: ', str(temp_state), '\nDepth :', depth)
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
            print(add_state)
            states_array.append(add_state)
    return states_array



"""
    empty() – Returns whether the stack is empty – Time Complexity : O(1)
    size() – Returns the size of the stack – Time Complexity : O(1)
    top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
    push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
    pop() – Deletes the top most element of the stack – Time Complexity : O(1)
"""