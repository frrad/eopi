def delete_node(node):
    node.value = node.next.value
    node.next = node.next.next
