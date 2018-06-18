def delete_minus_k(ll, k):
    if k == 1:
        ll.next.next.next = None
        return ll
    if k == 2:
        ll.next.next = ll.next.next.next
        return ll
    ll.next.next.next.next = ll.next.next.next.next.next
    return ll
