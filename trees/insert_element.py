"""
An algorithm for inserting an element in a binary tree.
Data Structure and Algorithmic Thinking with Python
Chapter 6, Problem 5, Page 144
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


def level_order_traversal(node):

    result = []
    queue = [node]

    while queue:
        node = queue.pop(0)
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


if __name__ == '__main__':

    n = Node(1)
    insert_element(n, 2)
    insert_element(n, 3)
    insert_element(n, 4)
    insert_element(n, 5)
    insert_element(n, 6)
    insert_element(n, 7)
    print(level_order_traversal(n))
