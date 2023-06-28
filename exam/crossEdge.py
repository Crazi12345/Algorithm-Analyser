import dictionaryGenerator

class Graph:
    def __init__(self, graph):
        self.time = 0
        self.traversal_array = []
        self.graph = graph
        self.v = len(graph)

    def print_graph(self):
        print("Graph Representation:")
        for key, value in self.graph.items():
            print(key, "-->", *value)
        print()

    def dfs(self):
        self.visited = {node: False for node in self.graph}
        self.start_time = {node: 0 for node in self.graph}
        self.end_time = {node: 0 for node in self.graph}

        for node in self.graph:
            if not self.visited[node]:
                self.traverse_dfs(node)
        print()
        print("DFS Traversal: ", self.traversal_array)
        print()

    def traverse_dfs(self, node):
        self.visited[node] = True
        self.traversal_array.append(node)
        self.start_time[node] = self.time
        self.time += 1
        for neighbour in self.graph[node]:
            if not self.visited[neighbour]:
                print('Tree Edge:', str(node)+'-->'+str(neighbour))
                self.traverse_dfs(neighbour)
            else:
                if self.start_time[node] > self.start_time[neighbour] and self.end_time[node] < self.end_time[neighbour]:
                    print('Back Edge:', str(node)+'-->'+str(neighbour))
                elif self.start_time[node] < self.start_time[neighbour] and self.end_time[node] > self.end_time[neighbour]:
                    print('Forward Edge:', str(node)+'-->'+str(neighbour))
                elif self.start_time[node] > self.start_time[neighbour] and self.end_time[node] > self.end_time[neighbour]:
                    print('Cross Edge:', str(node)+'-->'+str(neighbour))
        self.end_time[node] = self.time
        self.time += 1


if __name__ == "__main__":
    nodes_dict = dictionaryGenerator.input_nodes()
    g = Graph(nodes_dict)
    g.print_graph()
    g.dfs()

