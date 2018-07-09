def repeated(words):
    distance = float(inf)
    d = {}
    for i, word in enumerate(words):
        if word in d:
            temp = d[word] - i
            if temp < distance:
                distance = temp
        d[word] = i
    return distance
