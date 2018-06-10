def find_cycle_naive(ll):
    prev_nodes = set()
    ll_cur = ll
    while ll_cur is not None:
        if ll_cur not in prev_nodes:
            prev_nodes.add(ll_cur)
            ll_cur = ll_cur.next
        else:
            return ll_cur
    return None