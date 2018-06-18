def cyclicQ(ll):
    da_node = ll
    sentient = ll
    poop = ll
    poop = poop.next.next
    ll = ll.next
    while poop != ll and poop is not None and poop.next is not None:
        poop = poop.next.next
        ll = ll.next
    
    if poop is None or poop.next is None:
        return None
    
    node_in_cycle = ll
    
    while ll.next != node_in_cycle:
        ll = ll.next
        da_node = da_node.next
    da_node = da_node.next

    while sentient != da_node:
        sentient = sentient.next
        da_node = da_node.next

    return da_node
