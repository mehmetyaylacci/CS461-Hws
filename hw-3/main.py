from tree import Tree

def tree_input(string):
  '''
  Function to take the input string and to check whether it follows the right format, and classifies the input for later interpretations
  '''
  answer_dictionary = {}
  num_only = True
  for i in string:
    if i not in '0123456789 ':
      num_only = False
      break
  if num_only:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    j = 0
    for i in string:
      if i.isnumeric():
        c = alphabet[j]
        answer_dictionary[c] = i
        j += 1
    if len(answer_dictionary.values()) == 9: 
      return answer_dictionary
    else:
      print("Please enter the values in the correct format")
      return None
  else:
    string = string.split(' ')
    split_string = []
    for x in string:
      split_string += x.split('=')
    index = 0
    while index < len(split_string):
      answer_dictionary[split_string[index]] = split_string[index + 1]
      index += 2
    return answer_dictionary


def minimax_rec( a_tree, depth, node, array):
  '''
  Recursive part of the minmax algorithm without implementing pruning
  '''
  if depth == 0:
    letter = node.letter
    return [node.data, letter]

  elif depth % 2 == 0:
    value = -float("inf") # arbitrary
    
    for child in node.children():
      next_value = minimax_rec(a_tree, depth - 1, child, array)
      
      if int(next_value[0]) > value:
        letter = next_value[1]
      
      value = max(value, int(next_value[0])) #if depth is even, it is a max level

    return [value, letter]

  else:
    value = float("inf") # arbitrary

    for child in node.children():
      next_value = minimax_rec(a_tree, depth - 1, child, array)
      
      if int(next_value[0]) < value:
        letter = next_value[1]

      value = min(value, int(next_value[0])) #if depth is odd, it is a min level

    return [value, letter]


def minimax( a_tree, DEPTH):
  '''
  Initiator function for the minimax algorithm
  '''
  answer = []

  value =  minimax_rec( a_tree, DEPTH - 1, a_tree.root, answer)

  print('Letter is: ' + value[1])
  print('Value is: ' + str(value[0]))

  return value


def alphabeta_rec(a_tree, depth, node, the_min, the_max, letter):
  '''
  Recursive alpha beta pruning algorithm
  '''
  if depth == 0:
    letter = node.letter
    return [node.data, letter]

  elif depth % 2 == 0:
    value = -float('inf')
    for child in node.children():
      value = max(value, int(alphabeta_rec(
          a_tree, depth - 1, child, the_min, the_max, letter)[0]))
      the_max = max(value[0], the_max)
      
      if the_max >= the_min:
        print(str(the_max), '>=', str(the_min))
        print('Pruned the value: ' + str(the_max))
        letter = value[1]
        break
    
    return [value, letter]
  
  else:
    value = float('inf')
    for child in node.children():
      value = min(value, int(alphabeta_rec(
          a_tree, depth - 1, child, the_min, the_max, letter)[0]))
      
      the_min = min(value, the_min)
      
      if the_max >= the_min:
        print(str(the_max), '>=', str(the_min))
        print('Pruned the value: ' + str(the_min))
        letter = value[1]
        break
    
    return [value, letter]

def alphabeta( a_tree, DEPTH):
  '''
  Function to initiate the recursive alphabeta pruning
  function
  '''
  return alphabeta_rec( a_tree, DEPTH - 1, a_tree.root, float('inf'), -float('inf'), '')
  # float('inf') represents an unbounded upper value for comparison, which is used to set the initial values of alpha and beta


# test data for the minimax (question 1 of minimax)
inp = 'A=5 B=3 C=1 D=2 E=5 F=4 G=1 H=3 I=3'
print("Current input :", inp)
inp = tree_input(inp)
T = Tree(inp)
print('Result from the minimax algorithm:', minimax(T, 3)[0])

# user input for the minimax algorithm (question 2 of minimax)
inp = str(input('Please enter 9 values in the domain Z, separated by spaces'))
print("Current input :", inp)
inp = tree_input(inp)
T = Tree(inp)
print('Result from the minimax algorithm:', minimax(T, 3)[0])

# test data for the alphabeta algorithm (question 1 of alphabeta)
inp = 'A=5 B=3 C=1 D=2 E=5 F=4 G=1 H=3 I=3'
print("Current input :", inp)
inp = tree_input(inp)
if inp != None:
  T = Tree(inp)
  print('Result from the alphabeta pruning algorithm:', alphabeta(T, 3))

# test data for the alphabeta algorithm (question 2 of alphabeta)
inp = 'A=5 B=2 C=2 D=5 E=1 F=3 G=2 H=4 I=2'
print("Current input :", inp)
inp = tree_input(inp)
T = Tree(inp)
print('Result from the alphabeta pruning algorithm:', alphabeta(T, 3))

# test data for the alphabeta algorithm (question 3 of alphabeta)
inp = 'A=1 B=3 C=4 D=1 E=4 F=1 G=3 H=5 I=3'
print("Current input :", inp)
inp = tree_input(inp)
T = Tree(inp)
print('Result from the alphabeta pruning algorithm:', alphabeta(T, 3))

# user input for the alphabeta algorithm (question 4 of alphabeta)
inp = str(input('Please enter 9 values in the domain Z, separated by spaces'))
print("Current input :", inp)
inp = tree_input(inp)
if inp != None:
  T = Tree(inp)
  print('Result from the alphabeta pruning algorithm:', alphabeta(T, 3))
