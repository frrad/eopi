def merge(arr, brr):
    ret = arr
    pos = -1

    for i, a in enumerate(arr):
        if a != 'x':
            pos += 1
            last_in_arr = i
    for i, b in enumerate(brr):
        pos += 1
        last_in_brr = i

    while pos >= 0:
        while last_in_arr >= 0 and last_in_brr >= 0:
            if arr[last_in_arr] > brr[last_in_brr]:
                ret[pos] = arr[last_in_arr]
                last_in_arr -= 1
                pos -= 1
            else:
                ret[pos] = brr[last_in_brr]
                last_in_brr -= 1
                pos -= 1
        
        if last_in_arr < 0:
            ret[pos] = brr[last_in_brr]
            last_in_brr -= 1
            pos -= 1
        else:
            ret[pos] = arr[last_in_arr]
            last_in_arr -= 1
            pos -= 1

    return ret
