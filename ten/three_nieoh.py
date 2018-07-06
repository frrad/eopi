import heapq

def almost_sorted(arr, k):
    H = arr[:k]
    heapq.heapify(H)
    ret = []

    while H:
        r = heapq.heappop(H)
        ret.append(r)
        if k < len(arr):
            heapq.heappush(H, arr[k])
            k += 1
    return ret
