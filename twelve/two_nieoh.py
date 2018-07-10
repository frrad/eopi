def anon(mag, letter):
    d = {}
    if len(letter) > len(mag):
        return False
    
    for l in letter:
        if l == ' ':
            continue
        if l in d:
            d[l] += 1
        else:
            d[l] = 1
    
    for m in mag:
        if m in d:
            d[m] -= 1
    for val in d.values():
        if val > 0:
            return False
    return True
