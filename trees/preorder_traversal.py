
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pre_order_recursive(root, result):

    result.append(root.data)
    if root.left: pre_order_recursive(root.left, result)
    if root.right: pre_order_recursive(root.right, result)
    return result


def pre_order_iterative(root):

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)

    return result


if __name__ == '__main__':

    t = Node(1)
    t.left = Node(2)
    t.right = Node(3)
    t.left.left = Node(4)
    t.left.right = Node(5)
    t.right.left = Node(6)
    t.right.right = Node(7)

    print(pre_order_recursive(t, []))
    print(pre_order_iterative(t))
