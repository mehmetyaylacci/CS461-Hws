#   example input:
#   A=5 B=3 C=1 D=2 E=5 F=4 G=1 H=3 I=3

from tree import Tree

def tree_input( string):
  string = string.split(' ')
  split_string = []

  for x in string:
    split_string += x.split('=')
  
  answer_dictionary = {}

  index = 0

  # print(split_string)

  while index < len(split_string):
    answer_dictionary[split_string[index]] = split_string[index + 1]
    index += 2
  
  # print(answer_dictionary)
  return answer_dictionary

# recursive minimax function that works like a human
# no pruning
def rec_minimax(passed_list, layer):
  i = 0
  res = []
  if layer != 0 and layer%2 == 0:
    while i < 3 ** layer:
      min_of_layer = min(passed_list[i:i+3])
      res.append(min_of_layer)
      i += 3
    if rec_minimax(res, layer-1):
      print(res)
    return False
  elif layer != 0 and layer%2 != 0:
    while i < 3 ** layer:
      max_of_layer = max(passed_list[i:i+3])
      res.append(max_of_layer)
      i += 3
    if rec_minimax(res, layer-1):
      print(res)
    return False
  else:
    return True

# warning, human like and no pruning
#rec_minimax(list_vals, 2)

# recursive part of the minmax algorithm wo pruning
def minimax_rec( a_tree, depth, node):
  if depth == 0:
    return node.data
  
  elif depth % 2 == 0:
    value = -100 # arbitrary
    
    for child in node.children():
      value = max(value, int(minimax_rec(a_tree, depth - 1, child))) 
    
    return value
  
  else:
    value = 100 # arbitrary

    for child in node.children():
      value = min(value, int(minimax_rec(a_tree, depth - 1, child)))
    
    return value

# minmax algorithm wo pruning
def minimax( a_tree, DEPTH):
  return minimax_rec( a_tree, DEPTH - 1, a_tree.root)

# test input
test = tree_input('A=5 B=3 C=1 D=2 E=5 F=4 G=1 H=3 I=3')
T = Tree(test)
print( minimax( T, 3))

def alphabeta_rec( a_tree, depth, node, min, max):
  if depth == 0:
    return node.data
  
  elif depth % 2 == 0:
    value = -100 # arbitrary
    
    for child in node.children():
      value = max(value, int(alphabeta_rec(a_tree, depth - 1, child, min, max))) 

      max = max(value, max)

      if max > min:
        break
    
    return value
  
  else:
    value = 100 # arbitrary

    for child in node.children():
      value = min(value, int(alphabeta_rec(a_tree, depth - 1, child, min, max)))
    
      min = min(value, min)

      if max > min:
        break

    return value

def alphabeta( a_tree, DEPTH):
  return alphabeta_rec( a_tree, DEPTH - 1, a_tree.root, 100, -100)

# test alphabeta
print( alphabeta( T, 3))