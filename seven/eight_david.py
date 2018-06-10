def remove_duplicates(ll):
    ll_cur = ll
    while ll_cur is not None and ll_cur.next is not None:
        if ll_cur.value == ll_cur.next.value:
            ll_cur.next = ll_cur.next.next
        ll_cur = ll_cur.next
    return ll