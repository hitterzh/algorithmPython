

class binary_search_tree:
    def __init__(self, val):
        self.right = None
        self.left = None
        self.val = val

    def append(self, node):
        if node.val > self.val:
            self.right = node
        else:
            self.left = node




