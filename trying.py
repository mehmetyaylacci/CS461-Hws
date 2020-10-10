# import matplotlib.pyplot as plt
import graph

"""
import Graph



G = nx.Graph()

G.add_node(a)
G.add_node(2)

G.add_edge(a,2)

nx.draw(G)
plt.draw()
plt.show()
"""

#firstState = state.State(3, 3, 0, 0, "left", 0)

while True:
  input_one = str(input('\nPlease enter the number of Missionaries and Cannibals (EXIT to exit): '))
  if input_one == 'EXIT':
    break
  else:
    if input_one.isnumeric():
      number = int(input_one)
      input_two = str(input('Please enter the capacity of the boat: '))
      if input_two.isnumeric():
        capacity = int(input_two)
        if (capacity >= 2 and number <= 3) or ((number == 4 or number == 5) and capacity == 3) or (capacity >= 4 and number >= 6):
          solver = graph.Graph() 
          solver.DFS_start(number, capacity)
        else:
          print('\nThis combination will not work! See why on https://arxiv.org/pdf/1802.09369.pdf\n')
      else:
        print('Please enter a valid number.')  
    else:
      print('Please enter a valid number.')