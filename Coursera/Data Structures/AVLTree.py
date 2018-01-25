class AVLTree:
	class Node:
		def __init__(self, data):
			self.data = data
			self.right = None
			self.left = None
			self.height = 1

	def get_balance(self, node):
		if not node:
			return 0

		return self.get_height(node.left) - self.get_height(node.right)

	def get_height(self, node):
		if not node:
			return 0

		return node.height

	def update_height(self, node):
		if not node:
			return

		node.height = max(get_height(node.left), get_height(node.right)) + 1

	def rotate_right(self, node):
		if not node:
			return node

		sub = node.left
		t2 = sub.right

		sub.right = node
		node.left = t2

		self.update_height(node)
		self.update_height(sub)

		return sub

	def rotate_left(self, node):
		if not node:
			return node

		sub = node.right
		t2 = sub.left

		sub.left = node
		node.right = t2

		self.update_height(node)
		self.update_height(sub)

		return sub

	def insert(self, root, data):
		if not root:
			return Node(data)
		elif data < self.root.data:
			root.left = self.insert(root.left, data)
		else:
			root.right = self.insert(root.right, data)

		root.height = self.update_height(root)
		balance = self.get_balance(root)

		# Case 1: Left-Left
		if balance > 1 and data < root.left.data:
			return self.rotate_right(root)

		# Case 2: Right-Right
		if balance < -1 and data > root.right.data:
			return self.rotate_left(root)

		# Case 3: Left-Right
		if balance > 1 and data > root.left.data:
			root.left = self.rotate_left(root.left)
			return self.rotate_right(root)

		# Case 4: Right-Left
		if balance < -1 and data < root.right.data:
			root.right = self.rotate_right(root.right)
			return self.rotate_left(root)
