# Partition a linked list around a value X
# All nodes less than X are to the left
# All nodes greater than or equal to X are to the right
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def printLL(head):
	while head:
		print(head.data)
		head = head.next

def partitionXInitial(head, x):
	if x <= 0 or head is None:
		return False

	curr = head
	while curr and curr.next:
		print("curr.data : {} and curr.next.data: {}".format(curr.data, curr.next.data))
		if curr.data >= x and curr.next.data < curr.data:
			curr.next.data, curr.data = curr.data, curr.next.data
			print("should swap these two: {} and {}".format(curr.next.data, curr.data))
		curr = curr.next

	return True

# Runtime: O(n)
# Space: O(1)

def partitionXFinal(head, x):
	if x <= 0 or head is None:
		return False

	begSmaller = Node(0)
	begLarger = Node(0)

	while head is not None:
		nextN = Node(head.next)
		if head.data < x:
			head.next = begSmaller
			begSmaller = head
		else:
			head.next = begLarger
			begLarger = head
		
		head = nextN

	start = begSmaller
	while begSmaller.next is not None:
		begSmaller = begSmaller.next

	begSmaller.next = begLarger

	return start

def partition(head, x):
    begSmaller = Node(0)
    endSmaller = begSmaller
    begLarger = Node(0)
    endLarger = begLarger
    curr = head
    
    while curr is not None:
        if curr.data < x:
            endSmaller.next = curr
            endSmaller = curr
        else:
            endLarger.next = curr
            endLarger = curr
        curr = curr.next
    endSmaller.next = begLarger.next
    endLarger.next = None
    
    return begSmaller.next

node1 = Node(1)
node2 = Node(12)
node3 = Node(9)
node4 = Node(4)
node5 = Node(3)
node6 = Node(6)
node7 = Node(2)
node8 = Node(8)
node9 = Node(7)
node10 = Node(100)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10
node10.next = None

#partitionXInitial(node1, 5)
#partitionXFinal(node1, 5)
partition(node1, 5)
printLL(node1)