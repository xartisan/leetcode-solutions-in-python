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
        dummy_node = ListNode(head.val - 1)
        dummy_node.next = head
        done = dummy_node
        cur = head.next
        last_node = head
        while cur:
            if cur.val != last_node.val:
                if last_node.next is cur:
                    done.next = last_node
                    done = last_node
                last_node = cur
            cur = cur.next
        if last_node.next is None:
            done.next = last_node
            done = last_node
        done.next = None

        return dummy_node.next