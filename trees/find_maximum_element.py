"""
An algorithm for finding the maximum element in a binary tree.
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_maximum_element_recursive(root):

    maximum = left = right = root.data

    if root.left:
        left = find_maximum_element_recursive(root.left)
    if root.right:
        right = find_maximum_element_recursive(root.right)

    return max(maximum, left, right)


def find_maximum_element_iterative(root):

    result = root.data
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node.data > result:
            result = node.data
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


if __name__ == '__main__':

    tree = Node(5)
    tree.left = Node(8)
    tree.right = Node(3)
    tree.left.left = Node(9)
    tree.left.right = Node(2)
    tree.right.left = Node(4)
    tree.right.right = Node(6)

    print(find_maximum_element_recursive(tree))
    print(find_maximum_element_iterative(tree))
