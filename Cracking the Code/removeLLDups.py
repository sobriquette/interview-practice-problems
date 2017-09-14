# Remove duplicates from unsorted linked list
# Assumptions:
# Can use extra DS
# Cannot sort

# Brute force #1
def removeDupsBrute1(head):
	if head is None:
		return
	
	curr = head

	while curr not None:
		runner = curr
		while runner not None:
			if runner.next.data == current.data:
				runner.next = runner.next.next
			else:
				runner = runner.next

# Runtime: O(n^2 + n)
# Space: O(n)

# Brute force #2
def removeDupsBrute2(head):
	if head is None:
		return
	
	found = {}
	prev = None
	curr = head
	
	while curr not None:
		if curr.data in found.has_key(curr.data):
			prevNode.next = currNode.next
		else:
			found[curr.data] = True
			prev = curr
		curr = curr.next

# Runtime: O(n^2)
# Space: O(2n)