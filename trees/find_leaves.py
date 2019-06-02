"""
An algorithm for finding the number of leaves in a tree
Data Structure and Algorithmic Thinking with Python
Chapter 6, Problem 14, Page 147
"""
from queue import Queue


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:

    def __init__(self, data):
        self.root = Node(data)

    def insert_element(self, value):
        queue = Queue()
        queue.put(self.root)
        while not queue.empty():
            node = queue.get()
            if node.left:
                queue.put(node.left)
            else:
                node.left = Node(value)
                return
            if node.right:
                queue.put(node.right)
            else:
                node.right = Node(value)
                return

    def level_order_traversal(self):
        result = []
        queue = Queue()
        queue.put(self.root)
        while not queue.empty():
            node = queue.get()
            result.append(node.data)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)

        print("Tree:", result)


def find_leaves(tree):

    q = Queue()
    q.put(tree.root)
    leaves = []
    leaf_count = 0

    while not q.empty():
        node = q.get()

        if node.left:
            q.put(node.left)

        if node.right:
            q.put(node.right)

        if not node.left and not node.right:
            leaf_count += 1
            leaves.append(node.data)

    print("Leaf Count:", leaf_count)
    print("Leaves:", leaves)


if __name__ == '__main__':

    t = Tree(1)
    t.insert_element(2)
    t.insert_element(3)
    t.insert_element(4)
    t.insert_element(5)
    t.insert_element(6)
    t.insert_element(7)
    t.level_order_traversal()
    find_leaves(t)

