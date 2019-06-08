def balanced(node):
    def get_height(node):
        if node is None:
            return True, 0
        lheight = 0
        rheight = 0
        left = get_height(node.left)
        right = get_height(node.right)
        if not left[0] or not right[0]:
            return False, 0
        lheight += left[1]
        rheight += right[1]
        if abs(lheight-rheight) > 1:
            return False, 0
        return True, max(lheight, rheight)
    return get_height(node)[0]
