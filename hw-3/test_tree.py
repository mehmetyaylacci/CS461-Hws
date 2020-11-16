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

d = tree_input("A=5 B=3 C=1 D=2 E=5 F=4 G=1 H=3 I=3")
T = Tree(d)
T.print_tree()

