# Time: O(n)
# Space: O(n)

# Recursive implementation
class Solution:
	def inorderTraversal(self, root):
		if not root:
			return []
		if not root.left and root.right:
			return [root.val]

		results = []
		self.inorderTraversalHelper(root, results)
		return results

	def inorderTraversalHelper(self, root, results):
		if not root.left and root.right:
			results.append(root.val)
			return root
		else:
			if root.left:
				self.inorderTraversal(root.left, results)
			results.append(root.val)
			if root.right:
				self.inorderTraversal(root.right, results)
			return root

	def inorderTraversalHelper2(self, root, results):
		if root:
			self.inorderTraversal(root.left, results)
			results.append(root.val)
			self.inorderTraversal(root.right, results)
			return root

# Iterative implementation
class Solution2:
	def inorderTraversal(self, root):
		if not root:
			return []

		stack, results = [], []
		node = root
		while True:
			while node:
				stack.append(node)
				node = node.left
			if not stack:
				return results
			node = stack.pop()
			results.append(node.val)
			node = node.right