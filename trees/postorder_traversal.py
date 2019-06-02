
class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def post_order_recursive(root, result):

    if root.left: post_order_recursive(root.left, result)
    if root.right: post_order_recursive (root.right, result)
    result.append(root.data)
    return result


def post_order_iterative(root):

    result = []
    visited = set()
    stack = []
    node = root

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.data)
                node = None

    return result


if __name__ == '__main__':

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)

    print(post_order_recursive(tree, []))
    print(post_order_iterative(tree))
