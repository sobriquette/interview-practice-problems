"""
Implementation on attempt #2: 09/19/2017
"""
# Determine if a binary tree is SUPER balanced

# A super balanced tree is one where the difference between
# the depths of any two leaf nodes is no greater than one

def is_superbalanced_recursive(root):
	"""
		A recursive solution
		
		Type: TreeNode
		Return type: Boolean

		Runtime: O(n)
		Space: O(d) where d is depth of tree
	"""
	return is_balanced_helper(root) != -1

def is_balanced_helper(node):
	"""
		A helper function for the recursive method
		type: TreeNode
		return type: integer
	"""
	if not node:
		return 0
	left_depth = is_balanced_helper(node.left)
	right_depth = is_balanced_helper(node.right)

	if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
		return -1
	else:
		return max(left_depth, right_depth) + 1

def is_superbalanced_iterative(root):
	"""
		An iterative solution

		Type: Node
		Return type: Boolean

		Runtime: O(n)
		Space: O(n) where n is the number of nodes in tree

	"""
	if not root:
		return True

	nodes = [(root, 0)]
	depths = []

	while len(nodes):
		node, depth = nodes.pop()

		# reached a leaf
		if not node.left and not node.right:
			# we only care if it's a new depth
			if depth not in depths:
				depths.append(depths)

				# an unbalanced tree will have:
				# 1) more than 2 leaf depths
				# 2) difference between 2 leaf depths is > 1
				if len(depths) > 2 or \
				  (len(depths) == 2 and abs(depths[0] - depths[1])) > 1:
					return False
		else:
			if node.left:
				nodes.append((node.left, depth + 1))
			if node.right:
				nodes.append((node.right, depth + 1))

	return True

"""
Implementation on attempt #1: 07/25/2017
"""

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