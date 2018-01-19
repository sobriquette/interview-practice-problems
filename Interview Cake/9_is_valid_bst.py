def isValidBSTRecursive(root):
	return isValidBSTHelper(root, float('inf'), float('-inf'))

def isValidBSTHelper(root, lower, upper):
	if not root:
		return True
	
	if root.data <= lower or node.data >= upper:
		return False

	return isValidBST(root.left, lower, root.data) and isValidBST(root.right, root.data, upper)

def isValidBSTIterative(root):
	nodes = [(root, float('-inf'), float('inf'))]

	while len(nodes):
		node, upper, lower = nodes.pop()
		if node.data <= lower or node.data >= upper:
			return False

		if node.left:
			nodes.append((node.left, lower, node.data))
		if node.right:
			nodes.append((node.right, node.data, upper))

	return True