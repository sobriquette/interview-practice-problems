def findRightmostNode(node):
	curr = node
	while curr:
		if not curr.right:
			return curr.value
		curr = curr.right

def get2ndLargest(root):
	if not root or (not root.left and not root.right):
		return "Must have at least 2 nodes"

	curr = root
	while curr:
		if curr.left and not curr.right:
			return findRightmostNode(curr.left)

		if curr.right and not curr.right.left and not curr.right.right:
			return curr.value

		curr = curr.right