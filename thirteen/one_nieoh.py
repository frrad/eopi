def intersect(arr, brr):
    ret = []
    if arr[0] > brr[0]:
        arr, brr = brr, arr

    a, b = 0, 0

    def eof(x, y):
        return x < len(arr) and y < len(brr)

    while a < len(arr) and b < len(brr):
        print a, b, arr, brr 
        while (arr[a] < brr[b]) or eof(a, b):
            a += 1
        while (arr[a] > brr[b]) or eof(a, b):
            print brr[b]
            b += 1
        if arr[a] == brr[b] and ret[-1:] != arr[a]:
            ret.append(arr[a])
        a += 1
    return ret
