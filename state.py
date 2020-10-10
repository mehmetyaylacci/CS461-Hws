class State:
    # temp values to help us initiate newer State objects
    temp_r_m = 0
    temp_r_c = 0
    temp_l_m = 0
    temp_l_c = 0
    temp_pos = ""

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

    # this will create the neighbor states however, we need to check
    # if possible
    def next_state_generator(self):
        for cannibal in range(self.boat):
            for missionary in range(self.boat):

                # we will make sure boat is possible here
                if missionary + cannibal <= self.boat and missionary >= cannibal:
                    
                    if self.boat_pos == "right":
                        self.temp_r_m -= missionary
                        self.temp_r_c -= cannibal
                        self.temp_l_m += missionary
                        self.temp_l_c += cannibal
                        self.temp_pos = "left"

                        yield State(self.temp_l_c, self.temp_l_m, self.temp_r_c, 
                            self.temp_r_m, self.temp_pos, self.boat)
                    
                    elif self.boat_pos == "left":
                        self.temp_r_m += missionary
                        self.temp_r_c += cannibal
                        self.temp_l_m -= missionary
                        self.temp_l_c -= cannibal
                        self.temp_pos = "right"

                        yield State(self.temp_l_c, self.temp_l_m, self.temp_r_c, 
                            self.temp_r_m, self.temp_pos, self.boat)
    
    # check if the 'self' state is the goal state
    def isGoalState(self):
      if self.left_c == 0 and self.left_m == 0: 
        return True
      else: 
        return False