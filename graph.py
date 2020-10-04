import networkx as nx

class Graph:
    G = nx.Graph()

    def __init__(self):
    
    def add_to_graph(self, starting_vertex, neighbor_vertex):
        G.add_node(neighbor_vertex)
        G.add_edge(starting_vertex, neighbor_vertex)