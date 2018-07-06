def symmetric(t):
    return mirrors(t.left, t.right)


def mirrors(l, r):
    if l is None and r is None:
        return True
    if l is None:
        return False
    if r is None:
        return False

    if l.data != r.data:
        return False

    return mirrors(l.left, r.right) and mirrors(l.right, r.left)
