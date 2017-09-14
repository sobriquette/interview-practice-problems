# A Queue is a first in, first out
# or FIFO structure
# Works just like a queue at a shop

class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self, item):
		self.items.pop()

	