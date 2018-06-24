class BinaryTree:
    
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self._parent = None
        self._left = None
        self._right = None
        
    def insert(self, key, val=None):
        if self.key is None:
            self.key = key
            self.val = val
            return self
        
        if key < self.key:
            if self._left is None:
                self._left = BinaryTree(key, val)
                self._left._parent = self
            else:
                self._left.insert(key, val)
        else:
            if self._right is None:
                self._right = BinaryTree(key, val)
                self._right._parent = self
            else:
                self._right.insert(key, val)
        
        return self
    
    def get_max_depth(self, prev_depth=0):
        if self._left is None:
            left_depth = prev_depth + 1
        else:
            left_depth = self._left.get_max_depth(prev_depth+1)
        
        if self._right is None:
            right_depth = prev_depth + 1
        else:
            right_depth = self._right.get_max_depth(prev_depth+1)
            
        depth = max(left_depth, right_depth)
        
        return depth
    
    def get_min_depth(self, prev_depth=0):
        if self._left is None or self._right is None:
            return prev_depth + 1
        else:
            return min(self._left.get_min_depth(prev_depth+1), self._right.get_min_depth(prev_depth+1))

        
def is_height_balanced(binary_tree):
    max_diff = binary_tree.get_max_depth() - binary_tree.get_min_depth()
    return max_diff <= 1
