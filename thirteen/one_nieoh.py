def intersect(arr, brr):
    ret = []
    last = ''
    if arr[0] > brr[0]:
        arr, brr = brr, arr

    a, b = 0, 0
    
    def eof(x, y):
        ret = (x < len(arr)) and (y < len(brr))
        return ret

    while a < len(arr) and b < len(brr):
        while eof(a, b) and (arr[a] < brr[b]):
            a += 1
        while eof(a, b) and (arr[a] > brr[b]):
            b += 1
        if eof(a,b) and arr[a] == brr[b] and last != arr[a]:
            ret.append(arr[a])
            last = arr[a]
        a += 1
    return ret
