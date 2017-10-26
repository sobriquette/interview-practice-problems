def dfs(origin):
	"""
		Baseline implementation of depth-first traversal
		for an undirected, connected graph

		Runtime: O(V + E)
		Space: O(1)
	"""
	# assuming there is a property "visited"
	origin.visited = True

	# assuming each node has a property "neighbors"
	# which is a list of adjacent nodes
	for node in origin.neighbors:
		if not node.visited:
			dfs(node)

def dfs_disconnected(graph, origin):
	"""
		Visit every vertex in the graph
		to capture all vertices in a disconneted graph

		Runtime: O(V + E)
		Space: O(1)
	"""
	for v in graph:
		if not v.visited:
			dfs(v)