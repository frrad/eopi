from collections import deque


def replace_and_remove(arr, size):
    num_processed = 0
    cur_ind = 0
    q = deque()

    while num_processed < size:
        cur_val = arr[cur_ind]
        if cur_val == 'a':
            q.append('d')
            q.append('d')
        elif cur_val != 'b':
            q.append(cur_val)
        arr[cur_ind] = q.popleft()
        num_processed += 1
        cur_ind += 1
    
    while len(q) > 0:
        arr[cur_ind] = q.popleft()
        cur_ind += 1
        
    return arr