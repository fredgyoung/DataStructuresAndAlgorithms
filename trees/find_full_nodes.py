from queue import Queue


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_full_nodes(root):

    q = Queue()
    q.put(root)
    full_nodes = 0

    while not q.empty():
        node = q.get()

        if node.left:
            q.put(node.left)

        if node.right:
            q.put(node.right)

        if node.left and node.right:
            full_nodes += 1

    return full_nodes


if __name__ == '__main__':

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)

    print(find_full_nodes(tree))
