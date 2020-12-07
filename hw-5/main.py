import math
from collections import defaultdict
# Node class
class Node:
  def __init__(self):
    self.data = [] # x, y, strval data[0] : [2]
    self.left = None
    self.right = None
    
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class Kd:
  def __init__(self, data):
    self.root = Node([1, 2, 'red'])
    self.data = data
    self.insert_kd_array()

  ###
  def insert_kd_array(self):
    for i in self.data:
      self.insert_kd(i)

  ### single-step
  def insert_kd(self, data):
    not_inserted = True
    depth = 0
    temp = self.root

    while(not_inserted):
      ###
      if depth % 2 == 0:
        if temp.data[0] <= data[0]:
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
      
      ###
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
  def postorder(self):
    temp = self.root
    print('Post')
    self.postorderTrav(temp)

  def inorder(self):
    temp = self.root
    print('Inorder')
    self.inorderTrav(temp)
  
  def postorderTrav(self, temp):
    if temp.left is not None:
      self.postorderTrav(temp.left)
    if temp.right is not None:   
      self.postorderTrav(temp.right)
    print(temp.data)

  def inorderTrav(self, temp):
    if temp.left is not None:
      self.inorderTrav(temp.left)
    print(temp.data)
    if temp.right is not None:   
      self.inorderTrav(temp.right)
  
  ###
  def kd_nearest_neighbor(self, query):
    not_found = True
    temp = self.root
    depth = 0
    dict_of_dist = {} # defaultdict(list)
    while not_found:
      if depth % 2 == 0:
        print("Comparing {0} and {1}".format(temp.data, query.data))
        if temp.data[0] <= query.data[0]:
          if temp.right != None:
            case = self.euc_dist(temp, query) 
            if case not in dict_of_dist.keys():
              dict_of_dist[case] = [temp]
            else:
              dict_of_dist[case].append(temp)
            temp = temp.right
          else:
            case = self.euc_dist(temp, query) 
            if case not in dict_of_dist.keys():
              dict_of_dist[case] = [temp]
            else:
              dict_of_dist[case].append(temp)
            not_found = False
        else:
          if temp.left != None:
            case = self.euc_dist(temp, query) 
            if case not in dict_of_dist.keys():
              dict_of_dist[case] = [temp]
            else:
              dict_of_dist[case].append(temp)
            temp = temp.left
          else:
            case = self.euc_dist(temp, query) 
            if case not in dict_of_dist.keys():
              dict_of_dist[case] = [temp]
            else:
              dict_of_dist[case].append(temp)
            temp = temp.right
            not_found = False
      elif depth % 2 == 1:
        print("Comparing {0} and {1}".format(temp.data, query.data))
        if temp.data[1] <= query.data[1]:
          if temp.right != None:
            case = self.euc_dist(temp, query) 
            if case not in dict_of_dist.keys():
              dict_of_dist[case] = [temp]
            else:
              dict_of_dist[case].append(temp)
            temp = temp.right
          else:
            case = self.euc_dist(temp, query) 
            if case not in dict_of_dist.keys():
              dict_of_dist[case] = [temp]
            else:
              dict_of_dist[case].append(temp)
            not_found = False
        else:
          if temp.left != None:
            case = self.euc_dist(temp, query) 
            if case not in dict_of_dist.keys():
              dict_of_dist[case] = [temp]
            else:
              dict_of_dist[case].append(temp)
            temp = temp.left
          else:
            case = self.euc_dist(temp, query) 
            if case not in dict_of_dist.keys():
              dict_of_dist[case] = [temp]
            else:
              dict_of_dist[case].append(temp)
            not_found = False
      depth += 1
    # print(dict_of_dist)
    end = min(dict_of_dist.keys())
    return self.closest_str(dict_of_dist[end][0], query)

  def closest_str(self, node1, node2):
    dist = self.euc_dist(node1, node2)
    fin_str = "Closest Neighbor Color : " + str(node1.data[2]) + "\nClosest Neighbor Coordinates : (" + str(node1.data[0]) + ", " + str(node1.data[1]) + ")\nClosest Neighbor Distance : " + str(dist) + "\n"
    return fin_str 

  def euc_dist(self, node1, node2):
    return math.sqrt( ((node2.data[0] - node1.data[0]) ** 2) + ((node2.data[1] - node1.data[1]) ** 2))

  def __str__(self):
    self.postorder() 
    self.inorder()

# main method
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
  print()
  kd.inorder()

  print(kd.kd_nearest_neighbor(Node([1, 4, "U1"])))
  print(kd.kd_nearest_neighbor(Node([1, 1, "U2"])))
  print(kd.kd_nearest_neighbor(Node([6, 6, "U3"])))
  print(kd.kd_nearest_neighbor(Node([6, 1, "U4"])))
  
if __name__ == "__main__":
  main()
