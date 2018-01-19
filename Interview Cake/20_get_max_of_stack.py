class MaxStack(object):
	def __init__(self):
		self.stack = Stack()
		self.max_val_states = Stack()

	def push(self, data):
		self.stack.append(data)

		# update max value if needed
		if data > self.max_val_states.peek() or not self.max_val_states:
			# add the new max to our max stack
			self.max_val_states.append(data)


	def pop(self):
		if self.stack:
			item = self.stack.pop()
			# check if the max value is being popped
			if self.max_val_states.peek() == item:
				# remove the element
				self.max_val_states.pop()

			return item
		else:
			raise IndexError("can't pop an empty stack!")

	def getMax(self):
		return self.max_val_states[-1]