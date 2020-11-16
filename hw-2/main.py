from puzzle import Puzzle
from asearch import A_search
import matplotlib.pyplot as plt 


'''
plots the graph of the max size of queue against state number, for the 10 states that are not solved by hand
'''
def plot_graph(y):
  x = [(i + 3) for i in range(10)]
  plt.bar(x, y, color ='blue', label="Graph")
  plt.xlabel("State Number")
  plt.ylabel("Max size of queue.")
  plt.legend()
  plt.xticks(range(3,13))
  plt.yticks(range(0, max(y)+2, 2))
  plt.show()


state_list = []
solver = A_search()

i = 1
print('Generated unique states')

# adds to the list of states for 12 times until 12 unique states are produced
while i <= 12:
  temp_puzzle = Puzzle()
  temp_puzzle.scramble()
  if temp_puzzle not in state_list and not (temp_puzzle.matrix == solver.end_matrix).all():
    state_list.append(temp_puzzle)
    i += 1

#S creates a dictionary for the 12 states
S = {}
for i in range (1, 13):
  S[i] = state_list[i-1]
  print('S' + str(i), '\n' + str(S[i].matrix))

print('\n\n\n\n--------------------------------------------------------\n\n\n\n')

# Solving S1 (fully traced)
print('S1 Before Solving')
print(S[1].matrix)
print('Solving S1')
solver.start_search(S[1])
solver.reset()

print('\n--------------------------------------------------------\n')

# Solving S2 (fully traced)
print('S2 Before Solving')
print(S[2].matrix)
print('Solving S2')
solver.start_search(S[2])

queue_sizes = []

for i in range(3, 13):
  solver.reset()
  queue_sizes.append(solver.queue_sizes(S[i]))

plot_graph(queue_sizes)
