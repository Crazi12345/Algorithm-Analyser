import dictionaryGenerator
#This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v)
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def fillOrder(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        stack.append(v)

    def getTranspose(self):
        g = Graph({node: [] for node in self.graph})

        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printSCCs(self):
        stack = []
        visited = {node: False for node in self.graph}

        for i in self.graph:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)

        gr = self.getTranspose()

        visited = {node: False for node in self.graph}

        while stack:
            i = stack.pop()
            if visited[i] == False:
                gr.DFSUtil(i, visited)
                print("")


# Here you can call your input_nodes function and pass the result to the Graph class.
nodes_dict = dictionaryGenerator.input_nodes()
g1 = Graph(nodes_dict)

print("Following are strongly connected components in given graph")
g1.printSCCs()
