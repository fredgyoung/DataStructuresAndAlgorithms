from queue import Queue


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_leaves(root):

    q = Queue()
    q.put(root)
    leaves = 0

    while not q.empty():
        node = q.get()

        if node.left:
            q.put(node.left)

        if node.right:
            q.put(node.right)

        if not node.left and not node.right:
            leaves += 1

    return leaves


if __name__ == '__main__':

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.right.right = Node(7)

    print(find_leaves(tree))
