"""
An algorithm for deleting a binary tree.
Data Structure and Algorithmic Thinking with Python
Chapter 6, Problem 9, Page 146
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def delete_tree(root):

    if root.left:
        if root.left.left or root.left.right:
            delete_tree(root.left)
        root.left = None

    if root.right:
        if root.right.left or root.right.right:
            delete_tree(root.right)
        root.right = None


if __name__ == '__main__':

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)

    try:
        tree
        print("tree exists")
    except NameError:
        print("tree doesn't exist")

    delete_tree(tree)
    del tree

    try:
        tree
        print("tree exists")
    except NameError:
        print("tree doesn't exist")
