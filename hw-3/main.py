#   example input:
#   A=5 B=3 C=1 D=2 E=5 F=4 G=1 H=3 I=3

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

# test input
test = tree_input('A=5 B=3 C=1 D=2 E=5 F=4 G=1 H=3 I=3')
# print(test)

list_vals = list(test.values())



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
rec_minimax(list_vals, 2)

def alphabeta( a_tree):
  root = a_tree.root

  queue = [root]

  # dfs logic
  while len(queue) > 0:
