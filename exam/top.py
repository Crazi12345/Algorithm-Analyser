from collections import defaultdict
import dictionaryGenerator

class Graph:
    def __init__(self, graph):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.letters = list(graph.keys())
        self.letter_map = {letter: index for index, letter in enumerate(self.letters)}

        for key, values in graph.items():
            for value in values:
                self.add_edge(key, value)

    def add_edge(self, u, v):
        self.graph[self.letter_map[u]].append(self.letter_map[v])

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)

        stack.insert(0, v)

    def topological_sort(self):
        visited = [False]*len(self.letters)
        stack = []

        for i in range(len(self.letters)):
            if visited[i] == False:
                self.topological_sort_util(i, visited, stack)

        print([self.letters[i] for i in stack])  # convert numeric indices back to letters


if __name__ == "__main__":
    nodes_dict = dictionaryGenerator.input_nodes()

    print("Topological Sort:")
    g = Graph(nodes_dict)
    g.topological_sort()

