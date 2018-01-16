class TrieNode:
	def __init__(self, data):
		self.data = data
		self.children = {}

class Trie:
	def __init__(self):
		self.head = TrieNode('*')

	def insert(self, data):
		node = self.head

		for d in data:
			if d in node.children:
				node = node.children[d]
			else:
				node.children[d] = TrieNode(d)
				node = node.children[d]

		# add flag for end of data
		node.children['*'] = '*'
