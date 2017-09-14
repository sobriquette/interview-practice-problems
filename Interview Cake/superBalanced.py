def isSuperBalancedRecursive(node):
	isBalanced = isSuperBalancedHelper(node, balanced)
	return True if isBalanced

def isSuperBalancedHelper(node, balanced):
	if not node.left and not node.right:
		return 0
	else:
		right = isSuperBalanced(node.right)
		left = isSuperBalanced(node.left)
		if abs(right - left) > 1:
			return False
		else:
			return max(right - left) + 1

def isSuperBalancedIterative(root):
	if not root:
		return True
	
	depths = []
	nodes = []
	nodes.append((root, 0))

	while len(nodes):
		node, depth = nodes.pop()

		if not node.left and not node.right:
			if depth not in depths:
				depths.append(depth)
				
				if len(depths) > 2 or (len(depths) == 2 and abs(depths[1] - depths[0]) > 1):
					return False
		else:
			if node.left:
				nodes.append(node.left, depth + 1)
			if node.right:
				nodes.append(node.right, depth + 1)

	return True