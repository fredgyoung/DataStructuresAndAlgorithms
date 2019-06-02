"""
An algorithm for comparing two trees
Data Structure and Algorithmic Thinking with Python
Chapter 6, Problem 17, Page 148
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

    def insert_elements(self, values):
        for v in values:
            queue = Queue()
            queue.put(self.root)
            while not queue.empty():
                node = queue.get()
                if node.left:
                    queue.put(node.left)
                else:
                    node.left = Node(v)
                    break
                if node.right:
                    queue.put(node.right)
                else:
                    node.right = Node(v)
                    break

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
        return


def compare_nodes(a, b):
    if not a.left and not a.right and not b.left and b.right and a.data == b.data: return True
    if a.data != b.data: return False
    if a.left and not b.left: return False
    if not a.left and b.left: return False
    if a.right and not b.right: return False
    if not a.right and b.right: return False
    left = compare_nodes(a.left, b.left) if a.left and b.left else True
    right = compare_nodes(a.right, b.right) if a.right and b.right else True
    return left and right


if __name__ == '__main__':

    t1 = Tree(Node(1))
    t1.insert_elements([2,3,4,5,6,7])
    t1.level_order_traversal()
    t2 = Tree(Node(1))
    t2.insert_elements([2,3,4,5,6,7])
    t2.level_order_traversal()
    t3 = Tree(Node(1))
    t3.insert_elements([2,3,4,5,7,6])
    t3.level_order_traversal()

    print("t1 == t2:", compare_nodes(t1.root, t2.root))
    print("t2 == t3:", compare_nodes(t2.root, t3.root))
