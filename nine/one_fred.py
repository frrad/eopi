def height_balanced(t):
    bal, h = bal_height(t)
    return bal


def bal_height(t):
    if t is None:
        return True, -1

    a, x = bal_height(t.left)
    b, y = bal_height(t.right)

    if not a or not b:
        return False, 99

    if abs(x - y) > 1:
        return False, 99

    return True, max(x, y) + 1
