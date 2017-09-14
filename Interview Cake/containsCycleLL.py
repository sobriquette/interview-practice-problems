# Determine if there is a cycle
def contains_cycle(node):
	if not node:
		return False

	slow = node
	fast = node

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

		if fast is slow:
			return True

	return False

"""
BONUS #1: Find the first node in the cycle
IDEA: 
- Reset the slow pointer to the beginning
- Keep the fast pointer where they first meet
- Now the two pointers are the correct N steps away
  so that they next time they meet, it is at the beginning
"""
def get_first_node_in_cycle(node):
	if not node:
		return None

	slow = node
	fast = node
	has_cycle = False

	# find out if there is a cycle
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

		if fast is slow:
			has_cycle = True
			break

	# find start of cycle if there is one
	if has_cycle:
		slow = node

		while fast and fast.next:
			slow = slow.next
			fast = fast.next

			if fast is slow:
				return slow
		return None
	else:
		return None

