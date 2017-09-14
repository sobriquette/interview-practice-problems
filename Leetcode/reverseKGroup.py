class Solution:
	def reverse_k_group(self, head, k):
		node = head

		while node:
			old_start = node
			prev = node
			next = node.next
			for i in range(k - 1):
				next.next, prev, next = prev, next, next.next
			old_start.next = next
			node = next