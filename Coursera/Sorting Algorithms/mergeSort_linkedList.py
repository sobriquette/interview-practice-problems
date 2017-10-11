class LinkedList:
	class Node:
		def __init__(self, data):
			self.data = data
			self.next = None

	def __init__(self):
		self.head = None

	def merge(left, right):
		result = None

		if not left:
			return right

		if not right:
			return left

		if left.data <= right.data:
			result = left
			result.next = merge(left.next, right)
		else:
			result = right
			result.next = merge(left, right.next)

		return result

	def merge_sort(n):
		if not n or not n.next:
			return n

		mid = get_mid(n)
		mid_next = mid.next

		mid.next = None

		left = merge_sort(n)
		right = merge_sort(mid_next)

		sorted_ll = merge(left, right)
		return sorted_ll

	def get_mid(n):
		if not n:
			return n

		fast = n.next
		slow = n

		while fast:
			fast = fast.next

			if fast:
				slow = slow.next
				fast = fast.next

		return slow

	def add(data):
		if not head:
			head = Node(data)

		new_node = Node(data)
		new_node.next = head
		head = new_node
