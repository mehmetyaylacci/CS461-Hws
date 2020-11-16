
class Tree:
  # create a tree
  def __init__(self, dict):
    self.root = self.Node()

    self.DEPTH = 2
    self.FIXED_NODES = 3

    stack_nodes = [self.root]

    # bfs logic
    current_node_count = 0
    while current_node_count < 4:
      temp = stack_nodes.pop(0)
      
      temp.left = self.Node()
      temp.middle = self.Node()
      temp.right = self.Node()
      
      stack_nodes.append(temp.left)
      stack_nodes.append(temp.middle)
      stack_nodes.append(temp.right)

      current_node_count += 1

    index = 0
    while index < len(stack_nodes):
      temp = stack_nodes.pop(0)

      print(dict.values())
      temp.data = dict.values()[index]
      temp.letter = dict.keys()[index]

      index += 1

  def print_tree(self):
    stack_nodes = [self.root]

    # bnf logic
    index = 0 
    while index < 9:
      temp = stack_nodes.pop(0)
      
      stack_nodes.append(temp.left)
      stack_nodes.append(temp.middle)
      stack_nodes.append(temp.right)

      print(temp.data)

      index += 1

  class Node:
      # create empty node
      def __init__(self):
        self.left = None
        self.middle = None
        self.right = None
        self.data = ''
        self.letter = ''
