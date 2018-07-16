# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def reversed_listnode(head, end):
        rv = None
        while head is not end:
            h = head
            head = head.next
            h.next = rv
            rv = h
        return rv

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy_node = ListNode(0)
        dummy_node.next = head
        end = dummy_node

        cur = head
        group = None
        group_size = 0
        while cur is not None:
            group_size += 1
            if group_size == 1:
                group = cur
            cur = cur.next

            if group_size == k:

                end.next = self.reversed_listnode(group, cur)
                end = group
                group = None
                group_size = 0

        if group_size > 0:
            end.next = group

        return dummy_node.next
