class BinaryTree:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    # Adds a left child with the given data if one does not already exist.a
    def add_left(self, data=None):
        if self.left is not None:
            return None

        new_left = BinaryTree(data)
        self.left = new_left
        return new_left

    # Adds a right child with the given data if one does not already exist.a
    def add_right(self, data=None):
        if self.right is not None:
            return None

        new_right = BinaryTree(data)
        self.right = new_right
        return new_right

    def __str__(self):
        l = 'X' if self.left is None else str(self.left)
        r = 'X' if self.right is None else str(self.right)
        return '(%s, %d, %s)' % (l, self.data, r)
