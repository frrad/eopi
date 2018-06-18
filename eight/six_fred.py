def sunset(landscape):
    ans = []
    for i, x in enumerate(landscape):
        if i + 1 == len(landscape) or x > max(landscape[i + 1:]):
            ans.append(x)
    return ans
