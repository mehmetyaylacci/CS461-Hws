'''
@authors: Burak Turksever, Eralp Kumbasar, Mehmet Yaylaci

Citation for the Code (The Graph Class)

Title: Toposort
Author: Peter Teichman   
Availability: https://gist.github.com/pteichman/618ee334321714590cd9

This code was adapted from the previously cited source. Adaptations
include the conversion of the method into a class method, hence make it
into a class rather than just keep it running with a dictionary 
'''

from collections import defaultdict

class Graph:
    # Constructor for the Graph class
    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V

    '''
    Adds an edge to the dictionary of the class
    Takes in 2 parameters -2 vertices-
    and adds it to the dictionary.
    '''
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)
        print("Added " + u + " to " + v, end = ", ")

    '''
    The topological sorting algorithm
    Uses the graph dictionary directly
    to topologically sort all the edges
    and returns the list in the correct order
    '''
    def topologicalSort(self):
        """Perform a topological sort on a graph
        This returns an ordering of the nodes in the graph that places all
        dependencies before the nodes that require them.
        Args:
            graph: an adjacency dict {node1: [dep1, dep2], node2: [dep1, dep3]}
        Returns:
            A list of ordered nodes
        """
        result = []
        used = set()

        def use(v, top):
            print("Visiting {}".format(v))

            if v in used:
                return

            for parent in self.graph.get(v, []):
                if parent is top:
                    raise ValueError("graph is cyclical through", parent)

                use(parent, v)

            print("Adding {}".format(v))
            used.add(v)
            result.append(v)

        for v in self.graph:
            use(v, v)

        return result[::-1]


print("\n\n")
g = Graph(8)
g.add_edge('fstream', 'iostream')
g.add_edge('ifstream', 'istream')
g.add_edge('ofstream', 'ostream')
g.add_edge('iostream', 'istream')
g.add_edge('iostream', 'ostream')
g.add_edge('istream', 'ios')
g.add_edge('ostream', 'ios')
g.add_edge('ios', 'everything')

print("\nFollowing is a Topological Sort of the given graph (fstream)\n")
for i in g.topologicalSort():
    print(i, end=", ")

print("\n\n")
g = Graph(10)
g.add_edge('Consultant Manager', 'Consultant')
g.add_edge('Consultant Manager', 'Manager')
g.add_edge('Director', 'Manager')
g.add_edge('Permanent Manager', 'Manager')
g.add_edge('Permanent Manager', 'Permanent Employee')
g.add_edge('Consultant', 'Temporary Employee')
g.add_edge('Manager', 'Employee')
g.add_edge('Permanent Employee', 'Employee')
g.add_edge('Temporary Employee', 'Employee')
g.add_edge('Employee', 'Everything')

print("\nFollowing is a Topological Sort of the given graph (Manager - Employee)\n")
for i in g.topologicalSort():
    print(i, end=", ")

print("\n\n")
g = Graph(19)
g.add_edge('Crazy', 'Professors')
g.add_edge('Crazy', 'Hackers')
g.add_edge('Jacque', 'Weigthlifters')
g.add_edge('Jacque', 'Shotputters')
g.add_edge('Jacque', 'Athletes')
g.add_edge('Professors', 'Eccentrics')
g.add_edge('Professors', 'Teachers')
g.add_edge('Hackers', 'Eccentrics')
g.add_edge('Hackers', 'Programmers')
g.add_edge('Weigthlifters', 'Athletes')
g.add_edge('Shotputters', 'Athletes')
g.add_edge('Weigthlifters', 'Endomorphs')
g.add_edge('Shotputters', 'Endomorphs')
g.add_edge('Eccentrics', 'Dwarfs')
g.add_edge('Teachers', 'Dwarfs')
g.add_edge('Programmers', 'Dwarfs')
g.add_edge('Endomorphs', 'Dwarfs')
g.add_edge('Athletes', 'Dwarfs')
g.add_edge('Dwarfs', 'Everything')

print("\nFollowing is a Topological Sort of the given graph (Crazy)\n")
for i in g.topologicalSort():
    print(i, end=", ")
