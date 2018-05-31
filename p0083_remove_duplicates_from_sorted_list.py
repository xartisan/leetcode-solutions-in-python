# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        dummy_node = ListNode(0)
        dummy_node.next = head
        done = dummy_node
        last = head
        cur = head.next

        while cur:
            if cur.val != last.val:
                done.next = last
                done = last
                last = cur

            cur = cur.next
        done.next = last 
        done = last
        done.next = None
        return dummy_node.next
