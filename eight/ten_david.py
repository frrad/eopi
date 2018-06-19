class Node:
    
    def __init__(self, val, next, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

        
class Queue:
    
    def __init__(self):
        self._back = None
        self._front = None
    
    def __str__(self):
        return '->'.join([str(val) for val in self.to_list()])
        
    def to_list(self):
        vals = []
        node = self._back
        while node is not None:
            vals.append(node.val)
            node = node.next
        return vals
        
    def enqueue(self, val):
        self._back = Node(val, self._back)
        if self._front is None:
            self._front = self._back
        else:
            self._back.next.prev = self._back
        return self
    
    def dequeue(self):
        val = self._front.val
        self._front = self._front.prev
        if self._front is None:
            self._back = None
        else:
            self._front.next = None
        return val


class MaxQueue1:
    
    def __init__(self):
        self._queue = Queue()
        self._max = None
    
    def __str__(self):
        return str(self._queue)
        
    def to_list(self):
        return self._queue.to_list()
        
    def enqueue(self, val):
        self._max = max(self._max, val)
        self._queue.enqueue(val)
        return self
    
    def dequeue(self):
        val = self._queue.dequeue()
        if val == self._max:
            self._max = max(self.to_list())
        return val
    
    def max(self):
        return self._max
    
    
class MaxQueue2:
    
    def __init__(self):
        self._stack1 = MaxStack3()
        self._stack2 = MaxStack3()
    
    def __str__(self):
        return str('->'.join([str(val) for val in self.to_list()]))
        
    def to_list(self):
        return self._stack1.to_list() + self._stack2.to_list()
        
    def enqueue(self, val):
        self._stack1.push(val)
        return self
    
    def dequeue(self):
        if self._stack2.peek() is None:
            while self._stack1.peek() is not None:
                self._stack2.push(self._stack1.pop())
        return self._stack2.pop()
    
    def max(self):
        return max(self._stack1.max(), self._stack2.max())