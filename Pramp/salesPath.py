class Node:
	def __init__(self, cost):
		self.cost = cost
		self.children = []
		self.parent = None

def get_cheapest_path_rec(root):
	if not root.children:
		return root.cost

	min_cost = float('inf')
	for child in root.children:
		curr_cost = get_cheapest_path(child)
		min_cost = min(min_cost, curr_cost)

	return min_cost + root.cost

def get_cheapest_cost_it(root):
	stack = [(root, root.data)]
	min_path = float('inf')

	while stack:
		node, curr_cost = stack.pop()
		
		if not node.children:
			min_path = min(min_path, curr_cost)
		else:
			for child in node.children:
				stack.append((child, child.data + curr_cost))

	return min_path