class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newData):
		self.data = newData

	def setNext(self, newNext):
		self.next = newNext

class UnorderedLinkedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return head is None

	def size(self):
		curr = self.head
		size = 0
		while curr:
			size += 1
			curr = curr.next
		return size

	def add(self, item):
		temp = Node(item)
		temp.next, self.head = self.head, temp
	
	def search(self, item):
		curr = self.head
		found = False

		while curr and not found:
			if curr.data == item:
				found = True
			else:
				curr = curr.next

		return found

	def remove(self, item):
		curr = self.head
		prev = None
		found = False

		while not found:
			if curr.data == item:
				found = True
			else:
				prev, curr = curr, curr.next

		if prev is None:
			self.head = curr.next
		else:
			prev.next = curr.next.next

class OrderedLinkedList:
	# same as unordered linked list
	# except for following:
	def search(self, item):
		curr = self.head
		found = False
		stop = False

		while curr and not found and not stop:
			if curr.data == item:
				found = True
			elif curr.data > item:
				stop = True
			else:
				curr = curr.next

	def add(self, item):
		curr = self.head
		prev = None
		stop = False

		while curr and not stop:
			if curr.data > item:
				stop = True
			else:
				prev, curr = curr, curr.next

		temp = Node(item)
		if prev is None:
			temp.next, self.head = self.head.next, temp
		else:
			temp.next, prev.next = curr, temp
