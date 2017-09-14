# Find kth to last element of singly linked list

# APPROACH #1: Brute force
# Get size of LL O(n)
# Run through LL for range size - k
# Runtime: O(n - k) if iterative
# Runtime: O(n^n - k) if recursive
# Space: O(n)

def getSize(node):
	if node is None:
		return 0
	else:
		getSize(1 + getSize(node.next))

def findKthBrute(head, k):
	if head is None:
		return 0

	el = head
	size = getSize(el)
	for i in range(size - k):
		el = el.next
	return el

# APPROACH #2: Math? Brute math?
# Have a turtle and hare
# Hare will be k faster than turtle
# When hare reaches None, turtle will be k from last
# Runtime: O(n)
# Space: O(1)

def findKthMath(head, k):
	if head is None or k <= 0:
		return None

	turtle = head
	hare = head

	for i in range(k):
		if hare is None:
			return None
		hare = hare.next

	if hare is None: return None

	while hare.next not None:
		turtle = turtle.next
		hare = hare.next

	return turtle