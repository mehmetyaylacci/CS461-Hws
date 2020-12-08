# @authors: 
# Burak Turksever
# Mehmet Yaylaci
# Eralp Kumbasar

import math

# Node class to initialize the nodes of the tree that will be constructed
class Node:
  '''
  The first initialization is to create a  node without any data in it, and without creating any neighboring nodes initially
  '''
  def __init__(self):
    self.data = [] # x, y, strval data[0] : [2]
    self.left = None
    self.right = None
    
  '''
  Defines the node with data inside, which will contain the width(x), length(y), and the color of the specific point in space
  '''
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

#Kd class to construct the k-d tree to solve the problem
class Kd:
  '''
  Creating a root node, chosen as the point (1,2) with the color red, and inputted a set of data with the information about the points in space and their corresponding colors
  '''
  def __init__(self, data):
    self.root = Node([1, 2, 'red'])
    self.data = data
    self.insert_kd_array()

  ###
  '''
  Function that inserts every data inside the data list to the kd tree
  '''
  def insert_kd_array(self):
    for i in self.data:
      self.insert_kd(i)

  ### single-step
  '''
  The function inserts each point's data to the tree. It compares the x or y value of the input to the corresponding data at the current node, depending on the depth currently searched in the tree.
  '''
  def insert_kd(self, data):
    not_inserted = True
    #the variable checks if the input has been inserted to the tree, if not, the variable is true, as set initially
    depth = 0
    temp = self.root#root node for initial comparison
    while(not_inserted):
      ###
      if depth % 2 == 0:
        if temp.data[0] <= data[0]:#if the x value of input is bigger than or equal to the x value at the node, the node is added to right
          if temp.right == None:
            temp.right = Node(data)
            not_inserted = False
            #if there are no nodes to the right, the input is added
            #the comparison starts again from the root node for the next value of input, with the previous input added to the right
          else:
            temp = temp.right
            #if there is a node to the right of the current one already, the comparison for the current input continues with the first node to the right of the current node evaluated in the tree
        #same procedure done for right is done for left,if the x value of input is less than the node that is compared with the input
        else:
          if temp.left == None:
            temp.left = Node(data)
            not_inserted = False
          else:
            temp = temp.left
      
      ###
      #same procedure but comparing for y for odd values of depth
      elif depth % 2 == 1:
        if temp.data[1] <= data[1]:
          if temp.right == None:
            temp.right = Node(data)
            not_inserted = False
          else:
            temp = temp.right
        
        else:
          if temp.left == None:
            temp.left = Node(data)
            not_inserted = False
          else:
            temp = temp.left
      
      depth += 1
      
  ###
  '''
  using post order traversal on the tree, in order to list the data starting from the left. Prints from the leftmost node of the tree, and applies post order traversal, ending with the root node of the tree.
  '''
  def postorder(self):
    temp = self.root
    print('\nPOST ORDER TRAVERSAL OF THE TREE\n')
    self.postorderTrav(temp)
    print("\nEND OF POST ORDER TRAVERSAL\n")
  
  def postorderTrav(self, temp):
    if temp.left is not None:
      self.postorderTrav(temp.left)
    if temp.right is not None:   
      self.postorderTrav(temp.right)
    print(temp.data)
  
  ###
  '''
  Function to calculate and output the nearest neighbor of the inputted function according to the k-d tree that was previously created.
  '''
  def kd_nearest_neighbor(self, query):
    not_found = True
    temp = self.root
    depth = 0
    dict_of_dist = {}
    while not_found:
      ###
      #adds the euclidian distance to the dictionary of distances
      case = self.euc_dist(temp, query) 
      if case not in dict_of_dist.keys():
        dict_of_dist[case] = [temp]
      else:
        dict_of_dist[case].append(temp)
      
      ###
      #similar procedure to the construction of k-d tree, without the input being added to the tree
      #x comparison for even depth, y comparison for odd depth
      if depth % 2 == 0:
        print("Comparing {0} and {1}".format(temp.data, query.data))
        if temp.data[0] <= query.data[0]:
          #when x value of input is bigger than the compared node in the tree
          if temp.right != None:
            temp = temp.right
            #if there are nodes to the right, the next node at the right is considered for comparison with the input
          else:
            not_found = False
            #when there is no node to evaluate at right, program exits the loop to return the current node in the tree as nearest neighbor
        else:
          #same procedure applied for left when the x value is bigger than 
          if temp.left != None:
            temp = temp.left
          else:
            not_found = False
      
      ###
      #same procedure for odd values of depth
      elif depth % 2 == 1:
        print("Comparing {0} and {1}".format(temp.data, query.data))
        if temp.data[1] <= query.data[1]:
          if temp.right != None:
            temp = temp.right
          else:
            not_found = False
        else:
          if temp.left != None:
            temp = temp.left
          else:
            not_found = False
      depth += 1
    #returns the closest distance to the input from a node in the tree
    end = min(dict_of_dist.keys())
    return self.closest_str(dict_of_dist[end][0], query)

  '''
  Function to return the closest neighbor and the distance to the closest neighbor from the input in string form.
  '''
  def closest_str(self, node1, node2):
    dist = self.euc_dist(node1, node2)
    fin_str = "Closest Neighbor Color : " + str(node1.data[2]) + "\nClosest Neighbor Coordinates : (" + str(node1.data[0]) + ", " + str(node1.data[1]) + ")\nClosest Neighbor Distance : " + str(dist) + "\n"
    return fin_str 

  #sqrt((x**2 + y**2)**2), returns euclidian distance, x and y differences between two x values and two y values
  def euc_dist(self, node1, node2):
    return math.sqrt( ((node2.data[0] - node1.data[0]) ** 2) + ((node2.data[1] - node1.data[1]) ** 2))

  def __str__(self):
    self.postorder()

# main method, enters each data to the k-d tree and finds the nearest neighbor to the input in the tree
def main():
  data = []
  data.append([2, 1, 'violet'])
  data.append([4, 2, 'blue'])
  data.append([6, 5, 'purple'])
  data.append([2, 5, 'orange'])
  data.append([5, 6, 'yellow'])
  data.append([2, 6, 'red'])
  data.append([6, 1, 'green'])
  kd = Kd(data)
  # kd.insert_random(data[0], data[1])
  kd.postorder()
  #4 questions solved
  print("Question 1")
  print(kd.kd_nearest_neighbor(Node([1, 4, "U1"])))
  print("Question 2")
  print(kd.kd_nearest_neighbor(Node([1, 1, "U2"])))
  print("Question 3")
  print(kd.kd_nearest_neighbor(Node([6, 6, "U3"])))
  print("Question 4")
  print(kd.kd_nearest_neighbor(Node([6, 1, "U4"])))
  print("Question 5")
  ta_input = input("Please enter 2 space seperated integers : ")
  print(ta_input.split(" "))
  ta_node = Node([int(ta_input.split(" ")[0]), int(ta_input.split(" ")[1]), "U5-TA"])
  print(kd.kd_nearest_neighbor(ta_node))
  
if __name__ == "__main__":
  main()
