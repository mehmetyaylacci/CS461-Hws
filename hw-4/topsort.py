'''
@authors: Burak Turksever, Eralp Kumbasar, Mehmet Yaylaci

Citation for the Code (The Graph Class)

Title: Iterative Topological Sort
Author: Shihab Shahriar Khan    
Date: Nov. 11, 2017
Availability: https://stackoverflow.com/questions/47192626/deceptively-simple-implementation-of-topological-sorting-in-python

This code was adapted from the previously cited source. Adaptations
include the conversion of the method into a class method, hence make it
into a class rather than just keep it running with a dictionary 
'''

from collections import defaultdict

class Graph:
    # Constructor for the Graph class
    def __init__(self):
        self.graph = {}
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
    Adds the last edge to the dictionary of the class
    Takes in the last vertex as the parameter
    and adds it to the dictionary
    '''
    def add_edge_last(self, u):
        self.graph[u] = []
        print("Added last node " + u)

    '''
    The topological sorting algorithm
    Uses the graph dictionary directly
    to topologically sort all the edges
    and returns the list in the correct order
    '''

    def top_sort(self, start):
        q = [start]
        ans = []
        path =  set()
        while q:
            v = q[-1]
            print("Visiting: " + v)
            path = path.union({v})  
            children = [x for x in self.graph[v] if x not in path]    
            if not children:
                ans = [v]+ans 
                q.pop()
            else: 
                q.append(children[0])
        print('\n---- OUTPUT ----\n')
        return ans


print("\n\n")
g = Graph()
g.add_edge('fstream', 'iostream')
g.add_edge('ifstream', 'istream')
g.add_edge('ofstream', 'ostream')
g.add_edge('iostream', 'istream')
g.add_edge('iostream', 'ostream')
g.add_edge('istream', 'ios')
g.add_edge('ostream', 'ios')
g.add_edge('ios', 'everything')
g.add_edge_last('everything')

print("\nFollowing is a Topological Sort of the given graph (fstream)\n")
for i in g.top_sort('fstream'):
    print(i, end=", ")

print("\n\n")
g = Graph()
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
g.add_edge_last('Everything')

print("\nFollowing is a Topological Sort of the given graph (Manager - Employee)\n")
for i in g.top_sort('Consultant Manager'):
    print(i, end=", ")

print("\n\n")
g = Graph()
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
g.add_edge_last('Everything')

print("\nFollowing is a Topological Sort of the given graph (Crazy)\n")
for i in g.top_sort('Crazy'):
    print(i, end=", ")
