from collections import defaultdict

class Graph:
	def __init__(self, num_vertices):
		self.v = num_vertices
		self.graph = defaultdict(list)

	def add_edge(self, u, v):
		self.graph[u].append(v)

	def find_parent(self, parent, node):
		# is not part of a subset
		if parent[node] == -1:
			return node
		# is part of a subset, 
		# so look for the parent of that subset
		if parent[node] != -1:
			return self.find_parent(parent, parent[node])

	def union(self, parent, node, adj_node):
		x_set = self.find_parent(parent, node)
		y_set = self.find_parent(parent, adj_node)
		parent[x_set] = y_set

	def has_cycle(self):
		parent = [-1] * self.v

		for node in self.graph:
			for adj_node in self.graph[node]:
				x = self.find_parent(parent, node)
				y = self.find_parent(parent, adj_node)

			if x == y:
				return True
			self.union(parent, x, y)
