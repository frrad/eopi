def merge_lists(a,k):
    b = a.next
    c = b.next
    d = c.next

    l = k.next
    m = l.next
    n = m.next
    
    a.next = k
    k.next = b
    b.next = c
    c.next = l
    l.next = m
    m.next = n
    n.next = d

    return a
