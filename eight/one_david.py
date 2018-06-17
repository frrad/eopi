class Node:
    
    def __init__(self, val, next):
        self.val = val
        self.next = next

        
class Stack:
    
    def __init__(self):
        self._tail = None
        
    def __str__(self):
        return '->'.join([str(val) for val in self.to_list()])
    
    def to_list(self):
        vals = []
        node = self._tail
        while node is not None:
            vals.append(node.val)
            node = node.next
        return vals[::-1]
        
    def push(self, val):
        self._tail = Node(val, self._tail)
        return self
    
    def pop(self):
        if self._tail is None:
            return None
        tail_val = self._tail.val
        self._tail = self._tail.next    
        return tail_val
    
    def peek(self):
        if self._tail is None:
            return None
        else:
            return self._tail.val
        
        
class MaxStack1:
    """
    time: O(1) push, O(N) pop
    space: O(N) overall, O(1) extra for max
    """
    
    def __init__(self):
        self._tail = None
        self._max = None
        
    def __str__(self):
        vals = []
        node = self._tail
        while node is not None:
            vals.append(str(node.val))
            node = node.next
        vals = vals[::-1]
        return '->'.join(vals)
        
    def push(self, val):
        self._tail = Node(val, self._tail)
        self._max = max(self._max, val)
        return self
    
    def pop(self):
        tail_val = self._tail.val
        self._tail = self._tail.next
        
        if self._tail is None:
            self._max = None
        elif tail_val == self._max:
            self._max = self._tail.val
            node = self._tail.next
            while node is not None:
                self._max = max(node.val, self._max)
                node = node.next
        
        return tail_val
        
    def max(self):
        return self._max
    

class MaxStack2:
    """
    time: O(1) push, O(1) pop
    space: O(N) overall, O(N) extra for max
    """
    
    def __init__(self):
        self._stack = Stack()
        self._max_stack = Stack()
        
    def __str__(self):
        return str(self._stack)
        
    def push(self, val):
        self._stack.push(val)
        if self._stack.peek() >= self._max_stack.peek():
            self._max_stack.push(val)        
        return self
    
    def pop(self):
        tail_val = self._stack.pop()
        if tail_val == self._max_stack.peek():
            self._max_stack.pop()
        return tail_val
        
    def max(self):
        return self._max_stack.peek()
    
    
class MaxStack3:
    """
    time: O(1) push, O(1) pop
    space: O(N) overall, O(1) extra for max
    """
    
    def __init__(self):
        self._tail = None
        self._max = None
        
    def __str__(self):
        vals = []
        node = self._tail
        while node is not None:
            vals.append(str(node.val))
            node = node.next
        vals = vals[::-1]
        return '->'.join(vals)
        
    def push(self, val):
        if self._max is None:
            self._max = val
        elif val > self._max:
            temp = 2 * val - self._max  # encode previous max in stored value
            self._max = val
            val = temp
        self._tail = Node(val, self._tail)
        return self
    
    def pop(self):
        tail_val = self._tail.val
        self._tail = self._tail.next
        if tail_val > self._max:
            prev_max = 2 * self._max - tail_val  # decode previous max      
            tail_val = self._max
            self._max = prev_max
        return tail_val
        
    def max(self):
        return self._max