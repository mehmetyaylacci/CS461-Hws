#iterative_version of the algorithm
def dfs_iterative(graph, start):
    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)

    return path

#recursive_version of the algorithm
def dfs_recursive(graph, vertex, path=[]):
    path += [vertex]

    for neighbor in graph[vertex]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)

    return path

graph = {}
matrix = []
vertex = []

n=int(input("Enter the number of vertexes: "))

#get the vertex list from the user
print("Enter the vertex list for adjancency matrix:")
for j in input():
    vertex.append(j)
print(vertex)

#get the adjacency matrix from the user
print("Enter the adjacency matrix:")
matrix = []
for i in range(n):
    matrix.append([int(j) for j in input().split()])

#create a dictionary for adjacency matrix
for i in range(n):
    lst=[]
    for j in range(n):
        if matrix[i][j]==1:
            lst.append(vertex[j])
    key = vertex[i]
    graph[key]=lst
    
print("The graph is ",graph)
print(dfs_recursive(graph, 'a'))
