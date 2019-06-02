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


if __name__ == '__main__':

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.print_graph()
