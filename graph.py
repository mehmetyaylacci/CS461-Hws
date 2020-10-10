from state import State
from time import sleep

class Graph:
  def DFS_start(self, number, boat_capacity):
    final_string = []
    existingStates = []
    start = State(number, number, 0, 0, "left", boat_capacity)
    goal_state_id = self.id_func(State(0, 0, number, number, "right", boat_capacity))
    self.DFS(start, 0, existingStates, goal_state_id, final_string)
    for i in range(len(final_string)-1, -1, -1):
      print(final_string[i])

  # recursive depth first search to traverse to the goal state
  def DFS(self, currState, depth, existingStates, goal_state_id, final_string):
    depth += 1
    next_states = self.next_state_gen(currState)
    # sleep(1)
    if self.id_func(currState) == goal_state_id:
      next_states = []
      return True
    else:
      existingStates.append(self.id_func(currState))
      for check_state in next_states:
        if self.id_func(check_state) in existingStates:
          next_states.remove(check_state)
      for temp_state in next_states:
        if self.id_func(temp_state) not in existingStates:
          if self.DFS(temp_state, depth, existingStates, goal_state_id, final_string):
            constructed_str = "\nDepth:" + str(depth) + "\nCurrent Node: " + str(temp_state) 
            final_string.append(constructed_str)
            return True
    return False
  
  def next_state_gen(self, passed_state):
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
            add_state = State(passed_state.left_c + left_c, passed_state.left_m + left_m, passed_state.right_c + right_c, passed_state.right_m + right_m, new_boat_pos, passed_state.boat)
            if add_state.check_possible():
              states_array.append(add_state)
    return states_array
            
  # identification function to identify known nodes 
  # works by concatenating the state missionary, 
  # cannibal and boat position values one after the other
  def id_func(self, passed_state):
    constructed_str = str(passed_state.left_c) + str(passed_state.left_m) + str(passed_state.right_c) + str(passed_state.right_m) + str(passed_state.boat_pos)
    return constructed_str


"""
    empty() – Returns whether the stack is empty – Time Complexity : O(1)
    size() – Returns the size of the stack – Time Complexity : O(1)
    top() – Returns a reference to the top most element of the stack – Time Complexity : O(1)
    push(g) – Adds the element ‘g’ at the top of the stack – Time Complexity : O(1)
    pop() – Deletes the top most element of the stack – Time Complexity : O(1)
"""