class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def enqueue(self, item):
		self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

def isValidInput(string, pos):
	# return False if does not meet criteria
	if string == "" or None:
		return False
	elif pos < 0 or None:
		return False
	elif '(' not in string or ')' not in string:
		return False
	else: 
		return True

## Currently only works for first opening ##
def findClosing1(string, pos):
	# return False if does not meet criteria
	if string == "" or None:
		return False
	if pos < 0 or None:
		return False

	# build stack and queue for opening and closing parens
	# will hold only indices
	opens = Stack()
	closes = Queue()

	for i in range(len(string)):
		if string[i] == '(':
			opens.push(i)
		if string[i] == ')':
			closes.enqueue(i)

	# if stack and queue are not same length,
	# or if either is empty,
	# then parens are not balanced
	# and we can return False
	if opens.size() != closes.size():
		return False
	if opens.isEmpty() or closes.isEmpty():
		return False

	found = False
	close = 0
	
	# return the closing paren position
	while not found and not opens.isEmpty() and not closes.isEmpty():
		if opens.pop() == pos:
			close = closes.dequeue()
			found = True
		else:
			closes.dequeue()

	return close

# Runtime: O(2n + 8)
# Space: O(n + m + 2)

def findClosing2(string, pos):
	# return False if does not meet criteria
	if isValidInput(string, pos):
		opens = Stack()
		i = pos
		found = False
		while i < len(string) and not found:
			if string[i] == '(':
				opens.push(i)
			if string[i] == ')':
				opens.pop()
			if opens.isEmpty():
				found = True
				return i
			i += 1
		return False

# Runtime: O(n + 7)
# Space: O(n)

def findClosingFinal(string, pos):
	# return False if does not meet criteria
	if isValidInput(string, pos):
		i = pos + 1
		matches = 1

		while matches != 0 and i < len(string):
			if string[i] == '(':
				matches += 1
			if string[i] == ')':
				matches -= 1
			if matches == 0:
				return i
			else:
				i += 1

		return False

def findClosingSolution(string, pos):
	opens = 0
	i = pos

	while i < len(string):
		char = string[i]

		if char == '(':
			opens += 1
		elif char == ')':
			if opens == 0:
				return i
			else:
				opens -= 1

		i += 1
	return False

# Runtime: O(n + 5)
# Space: O(1)

if __name__=="__main__":
	string = [	"Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.",
				"    ",
				" what is this ",
				"(only(parens(everywhere()",
				"this matches ((()()()()))"	]
	pos = [10, -12, 0, 23, 19]
	for i in range(len(string)):
		#print(findClosing1(string[i], pos[i]))
		#print(findClosing2(string[i], pos[i]))
		print(findClosingFinal(string[i], pos[i]))