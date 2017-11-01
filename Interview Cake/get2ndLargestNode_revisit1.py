def find_largest(root):
	if not root:
		raise Exception('Tree must have at least 1 node')

	curr = root
	while curr.right:
		curr = curr.right

	return curr.data

def find_second_largest(root):
	if not root or (not root.left and not root.right):
		raise Exception('Tree must have at least 2 nodes')

	curr = root

	while curr:
		if curr.left and not curr.right:
			return find_largest(curr)
		if curr.right and not curr.right.left and not curr.right.right:
			return curr.data

		curr = curr.right