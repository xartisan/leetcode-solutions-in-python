# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(0)
        dummy_node.next = head
        cur = dummy_node
        first = head
        sign = False
        while first is not None:
            if sign:
                tail = first.next
                cur.next.next = tail
                first.next = cur.next
                cur.next = first
                first = tail
                cur = cur.next.next
            else:
                first = first.next
            sign = not sign
        return dummy_node.next

