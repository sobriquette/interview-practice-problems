# Tree traversals

def inorder(root):
	"""
		Baseline implementation of inorder traversal
		Visits left node before root, then right node last.
	
		Runtime: O(n) -- must visit each node in tree
		Space: O(1)
	"""
	if root:
		inorder(root.left)
		visit(root)
		inorder(root.right)

def preorder(root):
	"""
		Baseline implementation of preorder traversal
		Visits root before left and right nodes.
	
		Runtime: O(n) -- must visit each node in tree
		Space: O(1)
	"""
	if root:
		visit(root)
		preorder(root.left)
		preorder(root.right)

def postorder(root):
	"""
		Baseline implementation of postorder traversal
		Visits left and right nodes before root node.
	
		Runtime: O(n) -- must visit each node in tree
		Space: O(1)
	"""
	if root:
		postorder(root.left)
		postorder(root.right)
		visit(root)