def look_and_say(n):
    if n == 1:
        return '1'
    def next(previous):
        start = 0
        end = 0
        ret = []
        while end < len(previous):
            while end < len(previous) and previous[start] == previous[end]:
                end += 1
            ret.append(str(end-start))
            ret.append(previous[start])
            start = end
        return ''.join(ret)
    return next(look_and_say(n-1))

