def BSTcheck(node):
    
    def BSTcheckMM(node):
        if node is None:
            return True, None, None
        # Look at right subtree
        check, min_rnode, max_rnode = BSTcheckMM(node.right)
        if not check:
            return False, None, None
        if min_rnode is not None and min_rnode.data < node.data:
            return False, None, None
        max_node = max_rnode or node 

        # Look at the left subtree
        check, min_lnode, max_lnode = BSTcheckMM(node.left)
        if not check:
            return False, None, None
        if max_lnode is not None and max_lnode.data > node.data:
            return False, None, None
        min_node = min_lnode or node

        return True, min_node, max_node


    return BSTcheckMM(node)[0]
