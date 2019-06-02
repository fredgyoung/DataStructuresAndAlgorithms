# Adjacency list for an undirected graph
class Vertex:

    def __init__(self, id):
        self.id = id
        self.neighbors = {}
        self.visited = False
        self.previous = None

    def add_neighbor(self, neighbor, weight=1):
        self.neighbors[neighbor] = weight


class Graph:

    def __init__(self):
        self.vertices = {}
        self.size = 0

    def add_vertex(self, id):
        self.vertices[id] = Vertex(id)

    def get_vertices(self):
        return self.vertices.keys()

    def add_edge(self, src, dst, weight=1):
        if src not in self.vertices:
            self.add_vertex(src)
        if dst not in self.vertices:
            self.add_vertex(dst)
        self.vertices[src].add_neighbor(self.vertices[dst], weight)

    def print_graph(self):
        for key, value in self.vertices.items():
            print(key)


def DFS(graph, start):
    pass


# def BFS(graph, start):
#
#     queue = [start]
#     visited = []
#
#     while queue:
#         current = queue.pop(0)
#         print(current, end=" ")
#         visited.append(current)
#         for edge in g.edges:
#             if edge[0] == current and \
#                     edge[1] not in queue and \
#                     edge[1] not in visited:
#                 queue.append(edge[1])


if __name__ == '__main__':

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    g.print_graph()

    #DFS(g, 0)
