# merge k sorted linked lists
# given a list of head nodes

# Time: TIME LIMIT EXCEEDED
# Space: O(n)
class Solution(object):
	def mergeKLists(self, lists):
		if not lists:
			return []
		if len(lists) < 2:
			return lists[0]

		for i in range(1, len(lists)):
			lists[0] = self.mergeTwoLists(lists[0], lists[i])

		return lists[0]

	def mergeTwoLists(self, l1, l2):
		head = tmp_final_head = ListNode(0)

		while l1 and l2:
			if l1.val < l2.val:
				tmp_final_head.next = l1
				l1 = l1.next
			else:
				tmp_final_head.next = l2
				l2 = l2.next
			
			tmp_final_head = tmp_final_head.next
			
		tmp_final_head.next = l1 or l2

		return head.next

# Time: O(nlogk)
# Space: O(n)
class Solution2(object):
	def mergeKLists(self, lists):
		if not lists:
			return []
		if len(lists) < 2:
			return lists[0]

		left, right = 0, len(lists) - 1

		while right > 0:
			if left >= right:
				left = 0
			else:
				lists[left] = mergeTwoLists(lists[left], lists[right])
				left += 1
				right -= 1

		return lists[0]

	def mergeTwoLists(self, l1, l2):
		head = tmp_final_head = ListNode(0)

		while l1 and l2:
			if l1.val < l2.val:
				tmp_final_head.next = l1
				l1 = l1.next
			else:
				tmp_final_head.next = l2
				l2 = l2.next
			
			tmp_final_head = tmp_final_head.next
			
		tmp_final_head.next = l1 or l2

		return head.next