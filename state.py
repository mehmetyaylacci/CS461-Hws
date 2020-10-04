class State:
    # temp values to help us initiate newer State objects
    temp_r_m = 0
    temp_r_c = 0
    temp_l_m = 0
    temp_l_c = 0
    temp_pos = ""

    # when we are comparing, compare people and the boat_pos
    def __init__(self, left_c, left_m, right_c, right_m, boat_pos, number, boat):
        self.left_c = left_c
        self.left_m = left_m
        self.right_m = right_m
        self.right_c = right_c
        self.boat_pos = boat_pos
        self.number = number
        self.boat = boat

    def check_possible(self):
        if self.left_c > self.left_m or self.right_c > self.right_m:
            return False
        else:
            return True
    
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
                            self.temp_r_m, self.temp_pos, self.number, self.boat)
                    
                    elif self.boat_pos == "left":
                        self.temp_r_m += missionary
                        self.temp_r_c += cannibal
                        self.temp_l_m -= missionary
                        self.temp_l_c -= cannibal
                        self.temp_pos = "right"

                        yield State(self.temp_l_c, self.temp_l_m, self.temp_r_c, 
                            self.temp_r_m, self.temp_pos, self.number, self.boat)