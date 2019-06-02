class Vertex:

    def __init__(self, id):
        self.id = id
        self.adjacent = []

    def addNeighbor(self, neighbor):
        self.adjacent.append(neighbor)


class Graph:

    def __init__(self, size):
        self.size = size
        self.vertices = []
        for i in range(size):
            self.addVertex(i)

    def addVertex(self, id):
        self.vertices.append(Vertex(id))

    def addEdge(self, src, dst):
        self.vertices[src].addNeighbor(dst)
        self.vertices[dst].addNeighbor(src)

    def printGraph(self):
        for vertex in self.vertices:
            print(vertex.id, end="")
            for neighbor in vertex.adjacent:
                print(" -> ", end="")
                print(neighbor, end="")
            print()


if __name__ == '__main__':

    g = Graph(5)
    g.addEdge(0, 1)
    g.addEdge(0, 4)
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 3)
    g.addEdge(3, 4)
    g.printGraph()
