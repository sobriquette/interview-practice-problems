# Delete a node in the middle of singly linked list
# Given only access to that node

# Approach:
# Copy node.next to given node
# Delete node.next
# Point given node.next to node.next.next

def delMidNode(n):
	if n is None or n.next is None:
		return False

	temp = n.next
	n.data = temp.data
	n.next = temp.next

	return True