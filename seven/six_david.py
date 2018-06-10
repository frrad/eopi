def delete_node(ll):
    ll.value = ll.next.value
    ll.next = ll.next.next