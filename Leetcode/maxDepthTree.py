class Solution:
	def maxDepth(self, root):
		if not root:
			return 0
		else:
			return max(maxDepth(root.left), maxDepth(root.right)) + 1