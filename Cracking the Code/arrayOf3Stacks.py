############################ PROBLEM ##################################
# Describe how you could use a single array to implement three stacks #
# Think about what we can know about the input and refine solution    #
#######################################################################

# Approach 1: Fixed Divison #
# Allocate a fixed amount of space for each Stack #
class ArrayAsStack:
	def __init__(self, n):
		self.stackSize = n/3
		self.stackPointers = [-1] * 3
		self.items = [ None ] * n

	def push(self, e, stackNum):
		# check if current stack will exceed its allocated space
		if self.stackPointers[stackNum] + 1 > self.stackSize:
			raise IndexError("Stack is out of space")
		# update value of array where stackPointer is to input
		self.items[self.topOfStacks(stackNum)] = e
		# increment stackPointer to next spot in array
		self.stackPointers[stackNum] += 1

	def pop(self, stackNum):
		if self.isEmpty(stackNum):
			raise IndexError("Trying to pop empty stack")
		# store value so we can return it later
		value = self.items[self.topOfStacks(stackNum)]
		# reset the value, not actually "popping"
		self.items[topOfStacks(stackNum)] = None
		# decrement stackPointer value
		self.stackPointers[stackNum] -= 1
		return value

	def peek(self, stackNum):
		return self.items[self.topOfStacks(stackNum)]

	def isEmpty(self, stackNum):
		return self.stackPointers[stackNum] == -1

	# gets absolute position of stack pointer in array
	def topOfStacks(stackNum):
		return self.size * stackNum + self.stackPointers[stackNum]

# Approach 2 : Flexible Division
# Use a list of stack pointers, a list of available slots, and a "free" value to track #
class ArrayAsStack:
    def__init__(self, n):
		self.items = [None] * n
		self.stackPointers = [-1] * 3
		# tracks free spaces in items array
		self.next = list(range(1, n))
		# indicates end of free list
		self.next[n - 1] = -1
		self.free = 0

    def push(self, e, stackNum):
		if self.isArrayFull():
			raise IndexError("Out of space")
		index = self.free
		# since next is 1 index ahead,
		# the next free slot available is next[index]
		self.free = self.next[index]
		# update next to the top of stack for stackNum
		self.next[index] = self.stackPointers[stackNum]
		# stack for stackNum gets the prev free slot
		self.stackPointers[stackNum] = index
		# add element to array
		self.items[index] = e

    def pop(self, e, stackNum):
		if isEmpty(stackNum):
			raise IndexError("Trying to pop empty stack")
		index = self.stackPointers[stackNum]
		# top of stack for stackNum is now the prev free slot
		self.stackPointers[stackNum] = next[index]
		# prev top of stack is added to beginning of free list
		next[index] = free
		free = i
		# return prev top element
		return self.items[index]

    def isArrayFull(self):
		return self.free == -1

    def isEmpty(self, stackNum):
		return self.stackPointers[stackNum] == -1
