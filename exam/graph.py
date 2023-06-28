import dictionaryGenerator
import datastructures



dict = dictionaryGenerator.input_nodes()
stk = datastructures.Stack()
deq = datastructures.Deque()
def bfs(graph, root):

    visited = set([root])
    deq.addFront(root)
    while not deq.isEmpty():
        vertex = deq.removeRear()
        print(str(vertex) + " ", end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                deq.addFront(neighbour) 

def dfs(graph, root):
    visited = set([root])
    stk.push(root)

    while not stk.is_empty():
        vertex = stk.pop()
        print(str(vertex) + " ", end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                stk.push(neighbour)
arr = {'a': ['b', 'c', 'd'], 'b': ['a', 'c'], 'c': ['a', 'b', 'e'], 'd': ['a'], 'e': ['c']}

bfs(dict,'a')
print()
dfs(dict,'a')
