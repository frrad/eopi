from linked_list import LinkedList

def delete_last_k(ll, k):
    fuck = ll
    poop = ll
    while k > 0:
        poop = poop.next
        k -= 1

    while poop.next is not None:
        poop = poop.next
        ll = ll.next
    ll.next = ll.next.next
    return fuck
