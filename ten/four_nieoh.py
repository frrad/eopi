import heapq

def distance(x, y, z):
    return -(x**2 + y **2 + z**2)

def closest_stars(stars, k):
    H = [(distance(*star), star) for star in stars[:k]]
    heapq.heapify(H)
    i = 0
    ret = []
    for star in stars:
        if i < k:
            i += 1
            continue
        if distance(*star) > H[0][0]:
            heapq.heappop(H)
            heapq.heappush(H, (distance(*star), star))
    while H:
        ret.append(heapq.heappop(H)[1])
    return ret

