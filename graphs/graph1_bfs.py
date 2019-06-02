# Adjacency list for an undirected graph
class Graph:

    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, id):
        self.vertices.append(id)

    def add_edge(self, src, dst):
        if src not in self.vertices:
            self.add_vertex(src)
        if dst not in self.vertices:
            self.add_vertex(dst)
        self.edges.append([src, dst])
        self.edges.append([dst, src])

    def print_graph(self):
        for vertex in sorted(self.vertices):
            print([vertex], end="")
            for edge in self.edges:
                if edge[0] == vertex:
                    print(" -> ", end="")
                    print(edge[1], end="")
            print()


def BFS(graph, start):

    queue = [start]
    visited = []

    while queue:
        current = queue.pop(0)
        print(current, end=" ")
        visited.append(current)
        for edge in g.edges:
            if edge[0] == current and \
                    edge[1] not in queue and \
                    edge[1] not in visited:
                queue.append(edge[1])


if __name__ == '__main__':

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)

    BFS(g, 0)
