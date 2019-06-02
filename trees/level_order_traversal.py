class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def level_order_traversal(root):

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node.data)
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

    print(level_order_traversal(tree))
