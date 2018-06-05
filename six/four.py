from collections import deque



def replace_and_remove(arr, size):
    q = deque()

    for i, c in enumerate(arr[:size]):
        if c == 'a':
            q.append('d')
            q.append('d')
        elif c != 'b':
            q.append(c)
        arr[i] = q.popleft()
    
    while len(q) > 0:
        i += 1
        arr[i] = q.popleft()
        
    return arr


def replace_and_remove_inplace(arr, size):
    # Get rid of b's first to make sure there's enough room for the extra d's
    replace_ind = 0
    for i, c in enumerate(arr[:size]):
        arr[i] = '_'
        if c != 'b':
            arr[replace_ind] = c
            replace_ind += 1
        else:
            size -= 1
    
    # Add in d's
    num_a = 0
    for i in range(size):
        if arr[i + num_a] == 'a':
            arr[i + num_a] = 'd'
            num_a += 1
            new_letter = 'd'
            for j in range(i + num_a, size + num_a):
                temp = arr[j]
                arr[j] = new_letter
                new_letter = temp
    
    return arr
