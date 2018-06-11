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


def find_loop_node(ll):
    ll_cur_slow = ll
    ll_cur_fast = ll.next
    while None not in [ll_cur_slow, ll_cur_fast]:
        if ll_cur_slow == ll_cur_fast:
            return ll_cur_slow
        ll_cur_slow = ll_cur_slow.next
        ll_cur_fast = ll_cur_fast.next
        ll_cur_fast = None if ll_cur_fast is None else ll_cur_fast.next
    return None


def find_loop_len(loop_node):
    len = 1
    cur_node = loop_node.next
    while cur_node != loop_node:
        len += 1
        cur_node = cur_node.next
    return len


def find_cycle_inplace(ll):
    loop_node = find_loop_node(ll)
    if loop_node is None:
        return None
    
    loop_len = find_loop_len(loop_node)
    
    ll1_cur = ll
    ll2_cur = ll
    for i in range(loop_len):
        ll2_cur = ll2_cur.next
    while ll1_cur != ll2_cur:
        ll1_cur = ll1_cur.next
        ll2_cur = ll2_cur.next
    
    return ll1_cur
