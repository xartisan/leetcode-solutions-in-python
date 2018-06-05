class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        return str(self.val) + (' -> ' + repr(self.next) if self.next else '')

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy_lt = ListNode(0)
        dummy_ge = ListNode(0)
        
        cur_lt = dummy_lt
        cur_ge = dummy_ge
        cur = head

        while cur:
            if cur.val < x:
                cur_lt.next = cur
                cur_lt = cur
            else:
                cur_ge.next = cur
                cur_ge = cur

            cur = cur.next
        cur_lt.next = dummy_ge.next
        cur_ge.next = None
        return dummy_lt.next