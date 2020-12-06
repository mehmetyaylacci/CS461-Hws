
# Node class
class Node:
  def __init__(self):
    self.data = []
    self.left = Node()
    self.right = Node()
    
  def __init__(self, data):
    self.data = data
    self.left = Node()
    self.right = Node()
  
  def set_data(self, data):
    self.data = data

  def get_data(self):
    return self.data

# Tree class
class Tree:
  def __init__(self):
    self.root = Node()
  
  def __init__(self, data):
    self.root = Node(data)

class Kd:
  def __init__(self):
    self.T = Tree()
  
  

# main method
def main():
  print("hello world!")

if __name__ == "__main__":
  main()
