import networkx as nx
import state
import matplotlib.pyplot as plt

a = state.State(2,2,2,2,"left",2,2)

G = nx.Graph()

G.add_node(a)
G.add_node(2)

G.add_edge(a,2)

nx.draw(G)
plt.draw()
plt.show()