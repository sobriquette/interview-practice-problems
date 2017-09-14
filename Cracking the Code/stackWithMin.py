############################ PROBLEM ###################################
# Design a stack with push(), pop(), and a min() function. Min returns #
# the smallest element in the stack. All fns should operate in O(1)    #
########################################################################

# Approach: have a separate list track the mins before a pop

class StackWithMin:
	def __init__(self):
		self.items = []
		self.mins = []

	def push(self, item):
		if item < self.min():
			self.mins.append(item)

		self.items.append(item)

	def pop(self):
		if self.isEmpty():
			raise IndexError("Trying to pop empty stack")
		else:
			value = self.items.pop()
			if value == min():
				self.mins.pop()

			return value

	def peek(self):
		return mins[len(self.mins) - 1]

	def isEmpty(self):
		return self.items == []

	def min(self):
		if self.isEmpty():
			return float('inf')
		else:
			return mins.peek()