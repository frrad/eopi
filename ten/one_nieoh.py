import heapq
import copy

def merge_sorted(butthole):
    seq = copy.deepcopy(butthole)
    H = []
    for i, s in enumerate(seq):
        H.append((s[0], i))
    heapq.heapify(H)
    ret = []
    while H:
        m = heapq.heappop(H)
        ret.append(m[0])
        seq[m[1]] = seq[m[1]][1:] 
        if seq[m[1]]:
            heapq.heappush(H, (seq[m[1]][0], m[1]))
    return ret
