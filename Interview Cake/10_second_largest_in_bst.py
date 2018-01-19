"""
Implementation on attempt #3: 10/28/2017
"""

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

"""
Implementation on attempt #2: 09/20/2017
"""

# Find the second largest element in a BST

class RecursiveSolution():
	def find_largest(node):
		if not root:
			raise Exception("Tree must have at least 1 node")

		if root.right:
			return self.find_largest(root.right)

		return root.value

	def find_second_largest(root):
		"""
			type: TreeNode
			return type: int

			runtime: O(h)
			space: O(h) for height of tree in call stack
		"""
		if not root or (not root.left and not root.right):
			raise Exception("Tree must have at least 2 nodes")

		# case: current node is the largest and has left subtree
		# second largest will be in left subtree
		if root.left and not root.right:
			return self.find_largest(root.left)

		# case: current node is parent of the largest
		# current node is second largest
		if root.right and not root.right.left and not root.right.right:
			return root.value

		# keep going right in all other cases
		return self.find_second_largest(root.right)

class IterativeSolution():
	def find_largest(root):
		node = root

		while node:
			if not node.right:
				return node.value

			node = node.right

	def find_second_largest(root):
		"""
			type: TreeNode
			return type: int

			runtime: O(h)
			space: O(1)
		"""
		if not root or (not root.left and not root.right):
			raise Exception("Tree must have at least 2 nodes")

		node = root

		while node:
			# case: node is largest and has left subtree
			# second largest is in left subtree
			if not node.right and node.left:
				self.find_largest(node.left)

			# case: node is parent of largest
			# node is second largest
			if node.right and not node.right.left and not node.right.right:
				return node.value

			# keep going right in all other cases
			node = node.right

"""
Implementation on attempt #1: 07/25/2017
"""
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
