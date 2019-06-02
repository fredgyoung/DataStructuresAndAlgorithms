"""
An algorithm for...
Data Structure and Algorithmic Thinking with Python
Chapter 6, Problem 13, Page 147
"""
from queue import Queue


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def level_order_traversal(root):
    result = []
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        print(node)
        result.append(node.data)
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)
    print(result)
    return result


def find_node_with_value(root, value):

    queue = Queue()
    queue.put(root)

    while not queue.empty():
        node = queue.get()
        if node.data == value:
            return node
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)

    # if node not found
    return False


def find_deepest_node(root):

    node = None
    q = Queue()
    q.put(root)

    while not q.empty():
        node = q.get()
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)

    return node


def delete_node(root, value):
    # find node with value
    a = find_node_with_value(root, value)
    # find deepest node
    b = find_deepest_node(root)
    print(a, b)
    # swap nodes
    a, b = b, a
    print(a, b)
    # delete node with value
    del a


if __name__ == '__main__':

    # This does not work yet
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    tree.left.right.left = Node(8)
    tree.right.left.left = Node(9)

    level_order_traversal(tree)
    delete_node(tree, 5)
    level_order_traversal(tree)

