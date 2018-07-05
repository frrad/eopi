from one_david import BinaryHeap

def sort_almost_sorted(vals, k):
    heap = BinaryHeap(min=True)
    sorted_vals = []
    
    for val in vals:
        heap.push(val)
        if heap.size > 2*k + 1:
            sorted_vals.append(heap.pop()[0])
            
    while heap.size > 0:
        sorted_vals.append(heap.pop()[0])
    
    return sorted_vals