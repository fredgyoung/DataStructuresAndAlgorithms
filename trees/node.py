

class Node:

    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left(self, node):
        self.left = node

    def get_left(self):
        return self.left

    def set_right(self, node):
        self.right = node

    def get_right(self):
        return self.right
