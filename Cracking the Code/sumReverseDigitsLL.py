from random import randint

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	# adds to beginning of list
	def add(self, newData):
		newNode = Node(newData)
		newNode.next = self.head
		self.head = newNode

	def addLists(self, l1, l2):
		prev = None
		temp = None
		carry = 0

		while l1 or l2:
			# set numbers to sum
			first = 0 if l1 is None else l1.data
			second = 0 if l2 is None else l2.data
			result = first + second + carry
			
			carry = 1 if result >= 10 else 0 # set carry over number
			
			# update result if greater than 10, and use remainder
			result = result if result < 10 else result % 10
			
			temp = Node(result) # create new node with result
			
			# if new node is the first in list, set as head
			if self.head is None:
				self.head = temp
			else:
				prev.next = temp

			prev = temp # set for next iteration
			
			# move l1 and l2 pointers to next nodes
			if l1 is not None:
				l1 = l1.next
			if l2 is not None:
				l2 = l2.next

		if carry > 0:
			temp.next = Node(carry)

	# Runtime: O(n)
	# Space: O(n)

	def addListsRecurse(self, l1, l2, front, carry):
		# done if lists are pointing to None and nothing left to carry
		if l1 == None and l2 == None and carry == 0:
			return None

		# create new node with carry
		result = Node(carry)

		# if new node is first in list, set as head
		if self.head is None:
			self.head = result
		else:
			front.next = result

		front = result
		# add carry, l1, and l2 data to total
		total = carry
		if l1 is not None:
			total += l1.data
		if l2 is not None:
			total += l2.data

		# get second digit
		result.data = total % 10

		if l1 is not None or l2 is not None:
			first = None if l1 is None else l1.next
			second = None if l2 is None else l2.next
			carry = 1 if total >= 10 else 0
			more = self.addListsRecurse(first, second, front, carry)

			front.next = more

		return front

	def reverseList(self):
		if self.head is None:
			return None

		prev = None
		curr = self.head

		while curr is not None:
			after = curr.next
			curr.next = prev
			prev = curr
			curr = after

		self.head = prev

	def printList(self):
		curr = self.head
		while curr:
			print(curr.data)
			curr = curr.next



if __name__=="__main__":
	l1 = LinkedList()
	l2 = LinkedList()

	# create first ll
	for i in range(4):
		l1.add(randint(0, 9))
	print("this is the first list: ")
	l1.printList()

	# create second ll
	for i in range(4):
		l2.add(randint(0, 9))
	print("this is the second list: ")
	l2.printList()

	output = LinkedList()
	#output.addLists(l1.head, l2.head)
	output.addListsRecurse(l1.head, l2.head, None, 0)
	print("this is the output list: ")
	output.printList()
	output.reverseList()
	print("this should be reversed: ")
	output.printList()