class Node:
	"""
	Node utility class for doubly-linked list
	"""
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class LinkedList:
	"""
	Implementation of a doubly-linked list
	for quick insertion and deletion
	"""
	def __init__(self):
		self.head = None
		self.tail = None

	def add_first(self, data):
		new_node = Node(data)

		if not self.head and not self.tail:
			self.head = self.tail = new_node
		else:
			new_node.next = self.head
			self.head = new_node

	def add_last(self, data):
		new_node = Node(data)

		if not self.head and not self.tail:
			self.head = self.tail = new_node
		else:
			new_node.prev = self.tail
			self.tail.next = new_node
			self.tail = new_node

	def remove_first(self):
		if not self.head:
			return None
		
		item = self.head
		if self.head == self.tail:
			self.head = None
			self.tail = None
		else:
			self.head = self.head.next
		return item

	def remove_last(self):
		if not self.tail:
			return None

		item = self.tail
		if self.head == self.tail:
			self.head = None
			self.tail = None
		else:
			self.tail = self.tail.prev
		return item

class Person:
	"""
	Mock-up of potential Person object
	"""
	def __init__(self, data, person_id):
		self.data = data
		self.person_id = person_id
		self.friends = []

	def get_id(self):
		return self.person_id

	def get_friends(self):
		return self.friends

class PathNode:
	"""
	Node class containing Person object data
	and the parent node
	"""
	def __init__(self, person, parent):
		self.person = person
		self.parent = parent

	def get_person(self):
		return self.person

class BFSData:
	"""
	Encapsulates data needed to perform BFS

	nodes_to_visit: frontier for bfs, operates as queue
	visited: dictionary for quick lookup of visited nodes
	size: tracks size of nodes_to_visit
	"""
	def __init__(self):
		self.nodes_to_visit = LinkedList()
		self.visited = {}
		self.size = 0

	def add_node_to_visit(self, person):
		source_path = PathNode(person, None)
		self.nodes_to_visit.add(source_path)
		self.visited[person.get_id()] = source_path
		self.size += 1

	def get_node_to_visit(self):
		self.nodes_to_visit.get_first()
		self.size -= 1

	def is_finished(self):
		return self.nodes_to_visit is None

def collapse(node, starts_with_root):
	"""
	Recreate path by backtracking from node
	"""
	path = LinkedList()
	while node:
		if starts_with_root:
			path.add_last(node.person)
		else:
			path.add_first(node.person)
		node = node.parent

	return path

def merge_paths(bfs1, bfs2, connection):
	"""
	Connect path from root --> collision with
	path from collision --> goal
	"""
	end1 = bfs1.visited[connection]
	end2 = bfs2.visited[connection]

	path1 = end1.collapse(false)
	path2 = end2.collapse(true)

	path2.remove_first()
	path1.add_last(path2)
	return path1

def search_level(people, primary, secondary):
	"""
	Build up frontier, including all nodes at level
	"""
	count = primary.size
	for i in range(count):
		path_node = primary.get_node_to_visit()
		person = path_node.get_person()
		friends = person.get_friends()

		for friend_id in friends:
			if friend_id not in primary.visited:
				friend = people[friend_id]
				nxt = PathNode(friend, path_node)
				primary.visited[friend_id] = nxt
				primary.add_node_to_visit(nxt)

	return None

def find_path_biBFS(people, source, dest):
	"""
	Performs bidirectional breadth-first search
	"""
	source_data = BFSData(people[source])
	dest_data = BFSData(people[dest])

	while not source_data.is_finished() and not dest_data.is_finished():
		collision = search_level(people, source_data, dest_data)
		if collision is not None:
			return merge_paths(source_data, dest_data, collision.get_id())

		collision = search_level(people, dest_data, source_data)
		if collision is not None:
			return merge_paths(source_data, dest_data, collision.get_id())
	return None
