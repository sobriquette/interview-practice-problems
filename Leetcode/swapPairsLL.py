class Solution(object):
    def swapPairs(self, head):
        if not head:
            return head
        
        slow = head
        fast = head.next
        return self.swapPairsHelper(slow, fast)
    
    def swapPairsHelper(self, n1, n2):
        if not n2:
            return n1
        elif not n2.next:
            n2.next = n1
            n1.next = None
            return n2
        else:
            curr = n1
            curr.next = self.swapPairsHelper(n2.next, n2.next.next)
            n2.next = curr
            return n2