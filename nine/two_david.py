def is_symmetric_crappy(binary_tree):
    current_nodes = [binary_tree]
    num_empty = 0
    
    while num_empy < len(current_nodes):
        for i in range(len(current_nodes) // 2):
            if current_nodes[i].key != current_nodes[len(current_nodes) - 1 - i].key:
                return False
        
        child_nodes = []
        num_empty = 0
        for node in current_nodes:
            num_empty += (node.left is None) + (node.right is None)
            child_nodes.extend([node.left, node.right])
        
        current_nodes = child_nodes
    
    return True