# Time: O(n)
# Space: O(logn)

class Solution:
	def isValidBST(self, root):
		return self.checkBST(root, float('-inf'), float('inf'))

	def checkBST(self, node, mini, maxi):
		if not node:
			return True

		if node.val <= mini or node.val > maxi:
			return False
		else:
			return  self.checkBST(node.left, mini, node.val) and \
					self.checkBST(node.right, node.val, maxi)