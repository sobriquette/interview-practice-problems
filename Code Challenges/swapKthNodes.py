class Solution:
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        new_head = head
        prev_beg, knode_beg = head, head
        prev_end, knode_end = head, head
        # get k from end node and its prev
        fast = head
        slow = head
        for i in range(1, k):
            fast = fast.next
        
        # since we moved k from beg,
        # this is our k_beg
        knode_beg = fast
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # now we are k from end,
        # so this is our k_end
        knode_end = slow
        # now we get prev nodes of
        # k_beg and k_end
        while prev_end:
            if prev_end.next and prev_end.next == knode_end:
                break
            if prev_beg.next and prev_beg.next != knode_beg:
                prev_beg = prev_beg.next
            prev_end = prev_end.next
        
        # get the next nodes of two knodes first
        next_beg = knode_beg.next
        next_end = knode_end.next
        
        # swap the two knodes we found
        knode_beg.next = next_end
        prev_end.next = knode_beg
        prev_beg.next = knode_end
        knode_end.next = next_beg
        
        return head
        