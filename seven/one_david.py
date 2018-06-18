from linked_list import LinkedList

def merge_lists(ll1, ll2):
    if ll2.value < ll1.value:
        ll1, ll2 = ll2, ll1
    ll1_cur = ll1
    ll2_cur = ll2
    
    while ll2_cur is not None:
        # Advance ll1 to just before ll2 becomes smaller
        while ll1_cur.next is not None and ll1_cur.next.value < ll2_cur.value:
            ll1_cur = ll1_cur.next
        
        # Add the rest of ll2 if at the end of ll1
        if ll1_cur.next is None and ll2_cur is not None:
            ll1_cur.next = ll2_cur
            break
        
        # Pop from ll2 and insert into ll1
        ll2_next = ll2_cur.next
        ll2_cur.next = ll1_cur.next
        ll1_cur.next = ll2_cur
        ll2_cur = ll2_next
            
    return ll1