class State(Enum):
	UNVISITED = -1
	VISITING = 0
	VISITED = 1

def find_build_order(projects, dependencies):
	graph = build_graph(projects, dependencies)
	return order_projects(graph.get_nodes())

def order_projects(projects):
	stack = []
	for project in projects:
		if project.state == State.UNVISITED:
			if not dfs(project, stack):
				return False

	return stack

def dfs(project, stack):
	if project.state == State.VISITING:
		return False

	if project.state == State.UNVISITED:
		project.state = State.VISITING
		children = project.get_children()

		for child in children:
			if not dfs(child, stack):
				return False

		project.state = State.VISITED
		stack.append(project)

	return True