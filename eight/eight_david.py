class CircularQueue1:
    
    def __init__(self, initial_capacity):
        self.initial_capacity = initial_capacity
        self._arr = [None] * initial_capacity
        self._head_ind = 0  # most recent
        self._tail_ind = 0  # least recent
        self._num_elements = 0
    
    def __str__(self):
        return '->'.join([str(val) for val in self.to_list()])
    
    def _advance_ind(self, ind):
        return ind + 1 if ind < len(self._arr) - 1 else 0
            
    def _resize_if_necessary(self):            
        if self._num_elements == len(self._arr):
            self._arr.append(None)
            if self._tail_ind > 0:
                for i in range(0, self._head_ind+1):
                    self._arr[i - 1], self._arr[i] = self._arr[i], None
                self._head_ind -= 1
                if self._head_ind < 0:
                    self._head_ind = len(self._arr) - 1
                
    def to_list(self):
        ind = self._tail_ind
        vals = []
        while True:
            vals.append(self._arr[ind])
            if ind == self._head_ind:
                break
            ind = self._advance_ind(ind)
        return vals[::-1]
        
    def enqueue(self, val):
        self._resize_if_necessary()
        if self._num_elements > 0:
            self._head_ind = self._advance_ind(self._head_ind)
        self._arr[self._head_ind] = val
        self._num_elements += 1
        return self
    
    def dequeue(self):
        val = self._arr[self._tail_ind]
        self._tail_ind = self._advance_ind(self._tail_ind)
        self._num_elements -= 1
        return val
    
    def get_num_elements(self):
        return self._num_elements
    
    
class CircularQueue2:
    
    def __init__(self, initial_capacity):
        self.initial_capacity = initial_capacity
        self._arr = [None] * initial_capacity
        self._head_ind = 0  # most recent
        self._tail_ind = 0  # least recent
        self._num_elements = 0
    
    def __str__(self):
        return '->'.join([str(val) for val in self.to_list()])
    
    def _advance_ind(self, ind):
        return ind + 1 if ind < len(self._arr) - 1 else 0
            
    def _resize_if_necessary(self):            
        if self._num_elements == len(self._arr):
            self._arr.extend([None] * self._num_elements)
            for i in range(self._tail_ind):
                self._arr[self._num_elements + i] = self._arr[i]
            self._head_ind = self._tail_ind + self._num_elements - 1
                
    def to_list(self):
        ind = self._tail_ind
        vals = []
        while True:
            vals.append(self._arr[ind])
            if ind == self._head_ind:
                break
            ind = self._advance_ind(ind)
        return vals[::-1]
        
    def enqueue(self, val):
        self._resize_if_necessary()
        if self._num_elements > 0:
            self._head_ind = self._advance_ind(self._head_ind)
        self._arr[self._head_ind] = val
        self._num_elements += 1
        return self
    
    def dequeue(self):
        val = self._arr[self._tail_ind]
        self._tail_ind = self._advance_ind(self._tail_ind)
        self._num_elements -= 1
        return val
    
    def get_num_elements(self):
        return self._num_elements