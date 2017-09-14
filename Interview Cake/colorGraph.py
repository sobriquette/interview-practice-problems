def color_graph(graph, colors):
	for node in graph:
		if node in node.neighbors:
			raise Exception('illegal color due to loop in graph at: %s' % node.label)
		# get a node's neighbors' colors as a set
		# so we can chek for illegal coloring in constant time
		illegal_colors = set([ neighbor_color for neighbor in node.neighbors if neighbor.color ])

		# assign first legal color
		for color in colors:
			if color not in illegal_colors:
				node.color = color
				break

# runtime: O(N + M) for n nodes and m edges
# space: O(D) for illegal_colors set if all neighbors have different colors