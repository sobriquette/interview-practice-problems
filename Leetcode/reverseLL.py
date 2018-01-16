class Solution:
	def reverse_list(self, node):
		if not node or not node.next:
			return node

		old_head = node
		curr = node
		next = node.next

		while next:
			next.next, curr, next = curr, next, next.next

		next = curr
		old_head.next = None

		return curr

	def reverse_list_2(self, node):
		prev = None
		curr = node
		while curr:
			nxt = curr.next
			curr.next = prev
			prev = curr
			curr = nxt

		return prev

	def reverse_list_recursive(self, node):
		return self.reverse_list_util(node)

	def reverse_list_util(self, node, prev=None):
		if not node:
			return prev
		else:
			next = node.next
			node.next = prev
			return self.reverse_list_util(next, node)
