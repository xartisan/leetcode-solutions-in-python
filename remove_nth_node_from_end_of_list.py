class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        # exchange time for space
        record = []
        cur = head
        while cur:
            length += 1
            record.append(cur)
            cur = cur.next
        
        target_index = length - n
        if target_index == 0:
            return head.next
        prev = record[target_index - 1]
        prev.next = record[target_index].next
        return head
