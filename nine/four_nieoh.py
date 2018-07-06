def LCA(node1, node2):
    l1, l2 = 0, 0
    n1, n2 = node1, node2

    while n1.parent is not None:
        n1 = n1.parent
        l1 += 1
    while n2.parent is not None:
        n2 = n2.parent
        l2 += 1
    if l2 > l1:
        node2, node1 = node1, node2
    diff = abs(l1-l2)
    while diff > 0:
        node1 = node1.parent
        diff -= 1
    while node1.parent is not None:
        if node1 == node2:
            return node1
        node1 = node1.parent
        node2 = node2.parent
    return node2
