# CTCI implementation of topological sort

class Graph:
	def __init__(self):
		self.nodes = []
		self.nodes_map = {}

	def get_or_create_node(name):
		if name not in nodes_map:
			node = Project(name)
			self.nodes.append(node)
			self.nodes_map[name] = [node]

		return nodes_map[name]

	def add_edge(start_key, end_key):
		start = self.get_or_create_node(start_key)
		end = self.get_or_create_node(end_key)

		start.add_neighbor(end)

	def get_nodes():
		return self.nodes

class Project:
	def __init__(self, name):
		self.children = []
		self.nodes_map = {}
		self.name = name
		self.dependencies = 0

	def add_neighbor(node):
		if node.get_name() not in nodes_map:
			self.children.append(node)
			self.nodes_map[node.get_name()] = node
			node.increment_dependencies()

	def increment_dependencies():
		self.dependencies += 1

	def decrement_dependencies():
		self.dependencies -= 1

	def get_name():
		return self.name

	def get_children():
		return self.children

	def get_num_dependencies():
		return self.dependencies

def add_nondependent(order, projects, offset):
	for project in projects:
		if project.get_num_dependencies() == 0:
			order[offset] = project
			offset += 1

	return offset

def build_graph(projects, dependencies):
	graph = Graph()
	for project in projects:
		graph.get_or_create_node(project)

	for dependency, follow in dependencies:
		graph.add_edge(dependency, follow)

	return graph

def order_projects(projects):
	order = [None] * len(projects)
	# add projects that have no dependencies
	end_of_list = add_nondependent(order, projects, 0)

	to_be_processed = 0
	while to_be_processed < len(order):
		current = order[to_be_processed]

		# found a circular dependency
		if current is None:
			return None

		children = current.get_children()
		for child in children:
			child.decrement_dependencies()

		end_of_list = add_nondependent(order, children, end_of_list)
		to_be_processed += 1

	return order

def find_build_order(projects, dependencies):
	graph = build_graph(projects, dependencies)
	return order_projects(graph.get_nodes())

