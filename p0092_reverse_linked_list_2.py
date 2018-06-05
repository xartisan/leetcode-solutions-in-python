class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        cur = head

        counter = 1
        while counter < m:
            prev, cur = cur, cur.next
            counter += 1
        reversed_last = cur
        while counter <= n:
            next_node = cur.next
            cur.next = prev.next
            prev.next = cur
            cur = next_node
            counter += 1
        reversed_last.next = cur
        return dummy.next