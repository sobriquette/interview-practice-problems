class AVLTree:
	class Node:
		def __init__(self, data):
			self.data = data
			self.right = None
			self.left = None
			self.height = 1

	def __init__(self, root=None):
		self.root = root

	def get_height(self, node):
		if not node:
			return 0

		return node.height

	def update_height(self, node):
		if not node:
			return

		node.height = max(get_height(node.left), get_height(node.right)) + 1

	def __rotate_right(self, node):
		if not node:
			return node

		sub = node.left
		t2 = sub.right

		sub.right = node
		node.left = t2

		self.update_height(node)
		self.update_height(sub)

		return sub

