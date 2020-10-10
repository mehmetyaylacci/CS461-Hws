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
    sleep(1)
    if currState.isGoalState():
      return True
    else:
      next_states = currState.next_state_generator()
      for temp_state in next_states:
        existingStates.append(temp_state)
        for check_state in existingStates:
          if check_state.left_c == temp_state.left_c and check_state.left_m == temp_state.left_m and check_state.right_c == temp_state.right_c and check_state.right_m == temp_state.right_m and check_state.boat == temp_state.boat:
            print('Current node: ', str(temp_state), '\nDepth :', depth)
            self.DFS(temp_state, depth, existingStates)
    return False  
  
  def next_state_generator():
    


"""
    empty() – Returns whether the stack is empty – Time Complexity : O(1)
    size() – Returns the size of the stack – Time Complexity : O(1)
    top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
    push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
    pop() – Deletes the top most element of the stack – Time Complexity : O(1)
"""