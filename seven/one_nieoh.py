import linked_list

def merge_two_lists(l1, l2):
    if l1.value <= l2.value:
        merged = l1
        l1 = l1.next
    else:
        merged = l2
        l2 = l2.next
    poop = merged
    while l1 is not None and l2 is not None:
        if l1.value <= l2.value:
            merged.next = l1
            merged = merged.next
            l1 = l1.next
        else:
            merged.next = l2
            merged = merged.next
            l2 = l2.next
    merged.next = l1 if l1 else l2
    return poop
