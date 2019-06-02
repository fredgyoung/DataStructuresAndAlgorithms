"""
An algorithm for finding the size of a binary tree.
Data Structure and Algorithmic Thinking with Python
Chapter 6, Problem 8, Page 145
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_element(node, value):

    queue = [node]

    while queue:
        node = queue.pop(0)

        if node.left:
            queue.append(node.left)
        else:
            node.left = Node(value)
            return

        if node.right:
            queue.append(node.right)
        else:
            node.right = Node(value)
            return


def reverse_level_order(root):

    result = []
    queue = [root]
    stack = []

    while queue:
        node = queue.pop(0)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
        stack.append(node)

    while stack:
        result.append(stack.pop().data)

    return result


if __name__ == '__main__':

    n = Node(1)
    insert_element(n, 2)
    insert_element(n, 3)
    insert_element(n, 4)
    insert_element(n, 5)
    insert_element(n, 6)
    insert_element(n, 7)
    print(reverse_level_order(n))
