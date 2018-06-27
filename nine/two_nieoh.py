def symmetric(node):

    def func(node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False

        ret1 = func(node1.left, node2.right)
        ret2 = func(node1.right, node2.left)
        ret3 = node1.data == node2.data

        return (ret1 and ret2 and ret3)
    return func(node.left, node.right)
