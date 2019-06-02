"""
An Tree class
Includes a basic Node class.
"""
from queue import Queue


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:

    def __init__(self, node):
        self.root = node

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
        print(result)
        return


if __name__ == '__main__':

    tree = Tree(Node(1))
    tree.insert_element(2)
    tree.insert_element(3)
    tree.insert_element(4)
    tree.insert_element(5)
    tree.insert_element(6)
    tree.insert_element(7)
    tree.level_order_traversal()
