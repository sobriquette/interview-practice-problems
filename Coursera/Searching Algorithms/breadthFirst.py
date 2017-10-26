def bfs(start):
	"""
		Baseline implementation of breadth-first search

		Runtime: O(V + E)
		Space: O(1)
	"""
	start.visited = True
	q = Queue()
	q.enqueue(start)

	while q:
		n = q.dequeue()
		for adj_node in n.neighbors:
			if not adj_node:
				q.enqueue(adj_node)
				adj_node.visited = True

class State(Enum):
	UNVISITED = 0
	VISITING = 1
	VISITED = 2

def bfs_find_node(g, start, end):
	"""
		Using BFS to find if there is a route
		between two nodes

		Runtime: O(V + E)
		Space: O(1)
	"""
	if start == end:
		return True

	# assuming graph g is represented as a dict of lists
	for v in g:
		v.state = State.UNVISITED

	start.state = State.VISITED
	q = Queue()
	q.enqueue(start)

	while q:
		n = q.dequeue()
		if n is not None:
			for adj_node in n.neighbors:
				if adj_node.state == State.UNVISITED:
					if adj_node == end:
						return True
					else:
						adj_node.state = State.VISITING
						q.enqueue(adj_node)
			n.state = State.VISITED

	return False