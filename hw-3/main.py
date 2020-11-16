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
print(test)

list_vals = list(test.values())


def rec_minimax(passed_list, layer):
  i = 0
  while i < 3 ** layer:
    min = []
    all.append(min(list_vals[i:i+3]))
    i += 3
    print(all)

#def MINIMAX():
