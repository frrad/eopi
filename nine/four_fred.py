def lca(a, b):
    ha, hb = height(a), height(b)

    # assume WLOG hb >= ha
    if hb < ha:
        ha, hb = hb, ha
        a, b = b, a

    diff = hb - ha
    while diff > 0:
        b = b.parent
        diff -= 1

    while b != a:
        b = b.parent
        a = a.parent

    return a


def height(x):
    h = 0
    while x.parent is not None:
        x = x.parent
        h += 1
    return h
