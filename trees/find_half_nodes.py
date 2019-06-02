from queue import Queue


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_half_nodes(root):

    q = Queue()
    q.put(root)
    half_nodes = 0

    while not q.empty():
        node = q.get()

        if node.left:
            q.put(node.left)

        if node.right:
            q.put(node.right)

        if node.left and not node.right:
            half_nodes += 1

        if not node.left and node.right:
            half_nodes += 1

    return half_nodes


if __name__ == '__main__':

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.right.right = Node(7)

    print(find_half_nodes(tree))
