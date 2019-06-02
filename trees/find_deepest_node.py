"""
An algorithm for...
Data Structure and Algorithmic Thinking with Python
Chapter 6, Problem 12, Page 147
"""
from queue import Queue


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_deepest_node(root):

    q = Queue()
    q.put(root)
    node = root.data

    while not q.empty():
        node = q.get()

        if node.left:
            q.put(node.left)

        if node.right:
            q.put(node.right)

    return node.data


if __name__ == '__main__':

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    tree.left.right.left = Node(8)
    tree.right.left.left = Node(9)

    print(find_deepest_node(tree))
