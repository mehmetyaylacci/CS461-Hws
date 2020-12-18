'''
@authors: Burak Turksever, Eralp Kumbasar, Mehmet Yaylaci

Citation for the Code (The Graph Class)

Title: Topological Sorting
Author: GeeksforGeeks    
Date: 05/10/2020
Availability: https://www.geeksforgeeks.org/topological-sorting/

This code was adapted from the previously cited source. Adaptations
include making the algorithm function with direct text inputs instead
of just numbered nodes and the addition of a function for the proper
output that is required by the task description.
'''

from collections import defaultdict 
  
# Class to represent a graph 
class Graph: 
    # Constructor
    def __init__(self,vertices): 
        self.graph = defaultdict(list)
        self.V = vertices 
        self.vertexes = []
        self.out = []
    
    def topologicalSortUtil(self,v,visited,stack): 
      '''
      Recursive topological sorting function for the proper traversal
      of the graph
      '''
      visited[v] = True
      for i in self.graph[v]: 
          if visited[i] == False: 
              self.topologicalSortUtil(i,visited,stack) 
      stack.insert(0, v)

    def topologicalSort(self):
      '''
      Topological sorting function that calls the recursive topological sort
      function
      ''' 
      visited = [False]*self.V 
      stack = [] 
      for i in range(self.V): 
          if i < len(self.out):
            print("Visiting: {} \n".format( self.out[ i]))
          if visited[i] == False: 
              self.topologicalSortUtil(i,visited,stack) 
      answer = []
      for index in range(self.V):
        temp = self.vertexes[stack[self.V - index - 1]]

        print("Adding: {} \n".format(temp))

        answer.append(temp)
      return answer
  

    def addEdge(self, u, v):
      '''
      Function to add an edge to the graph as well as to the
      vertex list in the form "child -> parent"
      Calls the addEdge_real function for the add edge functionality 
      '''
      self.addEdge_real(u,v)      
      self.vertexes.append(str(u) + ' -> ' + str(v))
      if str(u) not in self.out:
        self.out.append(u)

    def addEdge_real(self,u,v): 
      '''
      Function to add an edge to the graph that is represented by a dictionary 
      that contains a list (the adjacency list)
      '''
      self.graph[u].append(v) 
      

g = Graph(8)
g.addEdge('fstream', 'iostream')
g.addEdge('iostream', 'istream')
g.addEdge('iostream', 'ostream')
g.addEdge('ifstream', 'istream')
g.addEdge('ofstream', 'ostream')
g.addEdge('istream', 'ios')
g.addEdge('ostream', 'ios')
g.addEdge('ios', 'everything')

print("\nFollowing is a Topological Sort of the given graph (fstream)\n")
print('---- OUTPUT STYLE #1 ----\n')
print(g.topologicalSort())
print('\n---- OUTPUT STYLE #2 ----\n')
g.out.append('Everything')
print(g.out)

g = Graph(10)
g.addEdge('Consultant Manager', 'Consultant')
g.addEdge('Consultant Manager', 'Manager')
g.addEdge('Director', 'Manager')
g.addEdge('Permanent Manager', 'Manager')
g.addEdge('Permanent Manager', 'Permanent Employee')
g.addEdge('Consultant', 'Temporary Employee')
g.addEdge('Manager', 'Employee')
g.addEdge('Permanent Employee', 'Employee')
g.addEdge('Temporary Employee', 'Employee')
g.addEdge('Employee', 'Everything')

print("\n\n\nFollowing is a Topological Sort of the given graph (Manager - Employee)\n")
print('---- OUTPUT STYLE #1 ----\n')
print(g.topologicalSort())
print('\n---- OUTPUT STYLE #2 ----\n')
g.out.append('Everything')
print(g.out)

g = Graph(19)
g.addEdge('Crazy', 'Professors')
g.addEdge('Crazy', 'Hackers')
g.addEdge('Jacque', 'Weigthlifters')
g.addEdge('Jacque', 'Shotputters')
g.addEdge('Jacque', 'Athletes')
g.addEdge('Professors', 'Eccentrics')
g.addEdge('Professors', 'Teachers')
g.addEdge('Hackers', 'Eccentrics')
g.addEdge('Hackers', 'Programmers')
g.addEdge('Weigthlifters', 'Athletes')
g.addEdge('Shotputters', 'Athletes')
g.addEdge('Weigthlifters', 'Endomorphs')
g.addEdge('Shotputters', 'Endomorphs')
g.addEdge('Eccentrics', 'Dwarfs')
g.addEdge('Teachers', 'Dwarfs')
g.addEdge('Programmers', 'Dwarfs')
g.addEdge('Endomorphs', 'Dwarfs')
g.addEdge('Athletes', 'Dwarfs')
g.addEdge('Dwarfs', 'Everything')

print("\n\n\nFollowing is a Topological Sort of the given graph (Crazy)\n")
print('---- OUTPUT STYLE #1 ----\n')
print(g.topologicalSort())
print('\n---- OUTPUT STYLE #2 ----\n')
g.out.append('Everything')
print(g.out)
