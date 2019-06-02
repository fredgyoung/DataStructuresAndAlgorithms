"""
An algorithm for finding the size of a binary tree.
Data Structure and Algorithmic Thinking with Python
Chapter 6, Problems 6 & 7, Page 145
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_size_recursive(root):

    left = right = 0

    if root.left:
        left = find_size_recursive(root.left)

    if root.right:
        right = find_size_recursive(root.right)

    return left + right + 1


def find_size_iterative(root):

    result = 0
    queue = [root]

    while queue:
        node = queue.pop(0)
        result += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


if __name__ == '__main__':

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    tree.right.left.right = Node(8)

    print(find_size_recursive(tree))
    print(find_size_iterative(tree))
