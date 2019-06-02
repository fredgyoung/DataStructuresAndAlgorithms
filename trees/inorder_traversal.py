
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order_recursive(root, result):

    if root.left: in_order_recursive(root.left, result)
    result.append(root.data)
    if root.right: in_order_recursive(root.right, result)
    return result


def in_order_iterative(root):

    result = []
    stack = []
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right

    return result


if __name__ == '__main__':

    t = Node(1)
    t.left = Node(2)
    t.right = Node(3)
    t.left.left = Node(4)
    t.left.right = Node(5)
    t.right.left = Node(6)
    t.right.right = Node(7)

    print(in_order_recursive(t, []))
    print(in_order_iterative(t))
