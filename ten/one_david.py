class BinaryHeap:
    
    def __init__(self, min=True):
        self.arr = []
        self.size = 0
        self._sign = 2*min - 1
        
    def _get_val(self, ind):
        return self.arr[ind][0]
        
    def push(self, val, data=None):
        val *= self._sign
        if self.size == len(self.arr):
            self.arr.append((val, data))
        else:
            self.arr[self.size] = (val, data)
        self.size += 1
        
        cur_ind = self.size - 1
        while cur_ind > 0:
            par_ind = cur_ind // 2
            if self._get_val(par_ind) > self._get_val(cur_ind):
                self.arr[par_ind], self.arr[cur_ind] = self.arr[cur_ind], self.arr[par_ind]
                cur_ind = par_ind
            else:
                break
                
        return self
    
    def pop(self):
        min_entry = (self.arr[0][0] * self._sign, self.arr[0][1])
        self.arr[0] = self.arr[self.size - 1]
        self.arr[self.size - 1] = '-'
        self.size -= 1
        
        cur_ind = 0
        while cur_ind <= self.size // 2:
            # Find index of smallest child
            child1_ind = (cur_ind + 1) * 2 - 1
            child2_ind = (cur_ind + 1) * 2
            if child1_ind < self.size:
                min_ind = child1_ind
            else:
                break
            if child2_ind < self.size:
                min_ind = min_ind if self._get_val(min_ind) < self._get_val(child2_ind) else child2_ind
            
            # Swap
            if self._get_val(cur_ind) > self._get_val(min_ind):
                self.arr[min_ind], self.arr[cur_ind] = self.arr[cur_ind], self.arr[min_ind]
                cur_ind = min_ind
            else:
                break

        return min_entry
    
    
    
def get_union(sorted_lists):
    """
    time: O{Nlog(M)}, where N is length of combined output list and M is number of input lists
    space: O{N}
    """
    heap = BinaryHeap(min=True)
    final_list = []
    
    for sorted_list in sorted_lists:
        heap.push(sorted_list[0], sorted_list[1:])
        
    while heap.size > 0:
        min_val, remaining_vals = heap.pop()
        final_list.append(min_val)
        if len(remaining_vals) > 0:
            heap.push(remaining_vals[0], remaining_vals[1:])
            
    return final_list