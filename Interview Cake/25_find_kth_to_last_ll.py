def get_kth_to_last_iterative(head, k):
	if not head:
		return head

	# determine length of list first
	length = 0
	curr = head
	while curr:
		curr = curr.next
		length += 1

	# if k > length, we can exit early
	if k > length:
		raise ValueError("k is too large")

	# now move node (length - k) steps forward
	# this is the node we want
	node = head
	for i in range(length - k):
		node = node.next

	return node