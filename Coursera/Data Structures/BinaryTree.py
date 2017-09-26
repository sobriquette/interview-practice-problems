class BinarySearchTree:
	# The Node class is internal to the Binary Search Tree class.
	class Node:
		def __init__(self, data):
			self.data = data
			self.left = left
			self.right = right

		def get_right(self):
			return self.right

		def get_left(self):
			return self.left

		def get_data(self):
			return self.data

		def set_right(self, new_right):
			self.right = new_right

		def set_left(self, new_left):
			self.left = new_left

		def __iter__(self):
			"""
				Performs an in-order traversal of the nodes.
			"""
			if self.left:
				for node in self.left:
					yield node

				yield self.data

			if self.right:
				for node in self.right:
					yield node

		def __repr__(self):
			return "BinarySearchTree.Node(" + repr(self.val) + ", " + repr(self.left) + ", " + repr(self.right) + ")"

	# Methods of Binary Search Tree class
	def __init__(self, root):
		self.root = None

	def insert(self, data):
		self.root = BinarySearchTree.__insert(self.root, data)

	def __insert(self, root, data):
		if not root:
			return BinarySearchTree.Node(data)

		if data < root.get_data():
			root.set_left(BinarySearchTree.__insert(root.get_left(), data))
		else:
			root.set_right(BinarySearchTree.__insert(root.get_right(), data))

	def __iter__(self):
		if self.root:
			return iter(self.root)
		else:
			return iter([])

	def __str__(self):
		return "BinarySearchTree(" + repr(self.root) + ")"

def main():
	s = input("Enter a list of numbers: ")
	l = s.split()

	tree = BinarySearchTree()

	for n in l:
		tree.insert(float(n))

	for node in tree:
		print(node)


if __name__=="__main__":
	main()
