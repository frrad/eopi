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


def node_in_loop(node, loop_node):
    test_node = loop_node.next
    while test_node != loop_node:
        if node == test_node:
            return True
        else:
            test_node = test_node.next
    return node == loop_node


def find_cycle_inplace(ll):
    loop_node = find_loop_node(ll)
    if loop_node is None:
        return None
    
    cur_node = ll
    while True:
        if node_in_loop(cur_node, loop_node):
            break
        cur_node = cur_node.next
    
    return cur_node
