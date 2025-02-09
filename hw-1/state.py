# @authors: 
# Burak Turksever
# Mehmet Yaylaci
# Eralp Kumbasar
class State:

    # constructor of the state class
    # takes the parameters: left Cannibals, left Missionaries,
    # right Cannibals right Missionaries, position of the boat
    # and the capacity of the boat 
    def __init__(self, left_c, left_m, right_c, right_m, boat_pos, boat):
        self.left_c = left_c
        self.left_m = left_m
        self.right_m = right_m
        self.right_c = right_c
        self.boat_pos = boat_pos
        self.boat = boat

    # toString function to get a nicely visualized output from
    # the state objects
    def __str__(self):
      return "\nLeft:(Cannibals: " + str(self.left_c) + " Missionaries: " + str(self.left_m) + ")\nRight:(Cannibals: " + str(self.right_c) + " Missionaries: " + str(self.right_m) + ")\n" + "Current Boat Position: " + str(self.boat_pos) + "\n"

    # the function used to check if a state is possible or not
    # gets rid of the negative states and states in which the
    # Cannibals outnumber the Missionaries
    def check_possible(self):
        if self.right_m < 0 or self.left_m < 0 or self.right_c < 0 or self.right_m < 0:
          return False
        elif self.left_c > self.left_m and self.left_m == 0:
          return True
        elif self.right_c > self.right_m and self.right_m == 0:
          return True 
        elif self.right_m == self.right_c and self.left_m == self.left_c:
          return True
        else:
          return False

    # check if the 'self' state is the goal state
    # hence check if all the Missionaries and Cannibals
    # passed to the right side of the river
    def isGoalState(self):
      if self.left_c == 0 and self.left_m == 0 and self.right_c == 3 and self.right_m == 3: 
        return True
      else: 
        return False