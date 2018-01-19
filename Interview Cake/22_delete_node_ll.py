def delete_node_in_ll(node):
	if node.next:
		node.data = node.next.data
		node.next = node.next.next
	else:
		raise Exception("can't delete this node!")