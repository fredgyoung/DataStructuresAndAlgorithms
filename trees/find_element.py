"""
An algorithm for finding a given element in a binary tree.
Data Structure and Algorithmic Thinking with Python
Chapter 6, Problems 3 & 4, Page 143
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_element_recursive(node, value):

    left = right = False

    if node.data == value:
        return True

    if node.left:
        left = find_element_recursive(node.left, value)

    if node.right:
        right = find_element_recursive(node.right, value)

    return left or right


def find_element_iterative(node, value):

    # Queue for BFS traversal
    queue = [node]

    while queue:
        node = queue.pop(0)
        if node.data == value:
            return True
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return False


if __name__ == '__main__':

    node = Node(5)
    node.left = Node(8)
    node.right = Node(3)
    node.left.left = Node(9)
    node.left.right = Node(2)
    node.right.left = Node(4)
    node.right.right = Node(6)

    print(find_element_recursive(node, 9))
    print(find_element_iterative(node, 9))
    print(find_element_recursive(node, 7))
    print(find_element_iterative(node, 7))
