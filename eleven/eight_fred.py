def kth_largest(l, k):
    x = l[:]
    x.sort(reverse=True)
    return x[k - 1]
