class Node():
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class TempTracker1():
	def __init__(self):
		self.t_sum = t_sum
		self.length = length
		self.temps_head = None
		self.temps_tail = None
		self.modes = {}
		self.most_appearances = 0

	def update(self):
		# update total
		self.t_sum += t
		# update length of linked list
		self.length += 1
		# update modes dict
		if t in self.modes:
			modes[t] += 1
		else:
			modes[t] = 1

		if modes[t] > most_appearances:
			most_appearances = modes[t]

	def insert(self, t):
		# update parameters
		self.update(t)

		# add new temperature to linked list
		if self.temps_head is None:
			self.temps_head = Node(t)
			self.temps_tail = self.temps_head
		else:
			prev = self.temps_head
			curr = self.temps_head.next
			while curr and t <= curr.data:
				prev = prev.next
				curr = curr.next

			new_t = Node(t, curr)
			prev.next = new_t

			# if current is None, that means the new node is the last node
			if not curr:
				self.temps.tail = new_t

	def min(self):
		return self.temps_head.data

	def max(self):
		return self.temps_tail.data

	def mean(self):
		return self.t_sum / self.length

	def mode(self):
		for k, v in self.modes.items():
			if v == self.most_appearances:
				return k

class TempTracker2():
	def __init__(self):
		self.t_sum = 0.0
		self.t_length = 0
		self.temps = [0] * 111
		self.max = float('inf')
		self.min = float('-inf')
		self.mode = [float('-inf'), float('-inf')]

	def insert(self, t):
		if t < 0 or t > 110:
			return "Please provide a valid temperature in (F)."

		# update parameters and temps array
		self.temps[t] += 1
		self.t_sum += t
		self.t_length += 1

		# check if there is a new max and/or min
		if t > self.max:
			self.max = t
		
		if t < self.min:
			self.min = t

		if self.temps[t] > self.mode[1]:
			self.mode = [t, self.temps[t]]

	def max(self):
		return self.max

	def min(self):
		return self.min

	def mean(self):
		return self.t_sum / self.t_length

	def mode(self):
		return self.mode[0]