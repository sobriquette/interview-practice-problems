def reverse_ll_recursive(curr, prev=None):
	if not curr:
		return prev

	# copy pointer to next element
	n = curr.next
	# reverse next pointer
	curr.next = prev
	# use n as current node and curr as previous
	return reverse_ll_recursive(n, curr)

def reverse_ll_iterative(head):
	curr = head
	prev, next = None, None

	while curr:
		# copy pointer to next element
		# before overwriting curr.next
		next = curr.next
		# reverse next pointer
		curr.next = prev
		# move forward
		prev = curr
		curr = next

	return prev