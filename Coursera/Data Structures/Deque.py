# A deque is a double-ended queue
# 1. It has 2 ends, a front and a rear
# 2. Items can be added or removed at either end
# 3. Does not require LIFO or FIFO orderings,
# 	 so we have to make consistent use of addition and removal

class Deque:
	def _init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	# O(n)
	def addRear(self, item):
		self.items.insert(0, item)
	# O(1)
	def addFront(self, item):
		self.items.append(item)
	# O(n)
	def removeRear(self):
		self.items.pop(0)
	# O(1)
	def removeFront(self):
		self.items.pop()

