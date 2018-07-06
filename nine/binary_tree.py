class BinaryTree(object):

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    # Adds a left child with the given data if one does not already exist.
    def add_left(self, data=None):
        if self.left is not None:
            return None

        new_left = type(self)(data)
        self.left = new_left
        return new_left

    # Adds a right child with the given data if one does not already exist.
    def add_right(self, data=None):
        if self.right is not None:
            return None

        new_right = type(self)(data)
        self.right = new_right
        return new_right

    def __str__(self):
        l = 'X' if self.left is None else str(self.left)
        r = 'X' if self.right is None else str(self.right)
        return '(%s, %d, %s)' % (l, self.data, r)
