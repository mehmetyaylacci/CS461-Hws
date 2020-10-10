class State:

    # when we are comparing, compare people and the boat_pos
    def __init__(self, left_c, left_m, right_c, right_m, boat_pos, boat):
        self.left_c = left_c
        self.left_m = left_m
        self.right_m = right_m
        self.right_c = right_c
        self.boat_pos = boat_pos
        self.boat = boat

        # self.temp_r_m = right_m
        # self.temp_r_c = right_c
        # self.temp_l_m = l
        # self.temp_r_m = right_m


    def __str__(self):
      return "\nLeft:(Cannibals: " + str(self.left_c) + " Missionaries: " + str(self.left_m) + ")\nRight:(Cannibals: " + str(self.right_c) + " Missionaries: " + str(self.right_m) + ")\n "

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
    def isGoalState(self):
      if self.left_c == 0 and self.left_m == 0 and self.right_c == 3 and self.right_m == 3: 
        return True
      else: 
        return False