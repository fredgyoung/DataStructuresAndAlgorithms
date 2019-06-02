"""
An algorithm for deleting a binary tree.
Data Structure and Algorithmic Thinking with Python
Chapter 6, Problems 10 & 11, Page 146
"""
from queue import Queue


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def tree_height_recursive(root):

    left = right = 0

    if root.left:
        left = tree_height_recursive(root.left)

    if root.right:
        right = tree_height_recursive(root.right)

    return max(left, right) + 1


def tree_height_iterative(root):

    q = Queue()
    q.put([root, 1])
    depth = 0

    while not q.empty():
        node, depth = q.get()

        if node.left:
            q.put([node.left, depth+1])

        if node.right:
            q.put([node.right, depth+1])

    return depth


if __name__ == '__main__':

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    tree.left.right.left = Node(8)

    print(tree_height_recursive(tree))
    print(tree_height_iterative(tree))
