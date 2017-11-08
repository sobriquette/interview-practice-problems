class Node:
	def __init__(self, cost):
		self.cost = cost
		self.children = []
		self.parent = None

def get_cheapest_path(root):
	if not root.children:
		return root.cost

	min_cost = float('inf')
	for child in root.children:
		curr_cost = get_cheapest_path(child)
		min_cost = min(min_cost, curr_cost)

	return min_cost + root.cost