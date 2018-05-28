# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head:
            return []
        cur = head
        length = 1
        while cur.next:
            length += 1
            cur = cur.next
        counter = length - k % length
        while counter > 0:
            cur = cur.next
            counter -= 1
        rv = cur.next
        cur.next = None
        return rv