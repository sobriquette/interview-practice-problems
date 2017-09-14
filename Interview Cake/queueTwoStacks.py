class QueueAsStack(object):
	def __init__(self):
		self.stack_in = Stack()
		self.stack_out = Stack()

	def enqueue(self, data):
		self.stack_in.push(data)

	def dequeue(self):
		# check if the second stack (for dequeuing) is empty.
		# if it is empty, we want to dump everything in first stack in.
		# that way when we dequeue, the first element pushed into stack 1,
		# is at the top of the stack.
		if self.stack_out.isEmpty():
			while not self.stack_in.isEmpty():
				self.stack_out.push(self.stack_in.pop())

			# check to see if stack 2 is still empty
			if self.stack_out.isEmpty():
				raise IndexError("can't dequeue from an empty stack!")
		
		# when we are done transferring elements,
		# or if that was not needed
		# return the top element on stack 2
		return self.stack_out.pop(data)
